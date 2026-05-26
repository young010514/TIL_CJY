SERVER_URL = "http://localhost:8080/api/v1";

const chatMain = document.querySelector(".chat-main");
const chatInput = document.querySelector(".chat-input");
const fileAddBtn = document.querySelector(".file-add-btn-wrapper");
const fileInput = fileAddBtn.querySelector(".file-add-btn > .file-input");
const filePreviewContainer = document.querySelector(".file-preview-container");
const chatUl = document.querySelector(".chat-ul");

/**
 * @typedef {Object} ParsedFileStrObj
 * @property {string} additionalData - 추가 데이터 문자열
 * @property {boolean} hasImage - 이미지 포함 여부
 */

/**
 * @typedef {Object} Chat - 채팅 메시지 객체 정의
 * @property {number} id - 메시지 고유 식별자
 * @property {string} role - 발신자 역할 (user, assistant 등)
 * @property {string} content - 메시지 내용
 */

/** @type {Chat[]} - Chat 객체 배열 */
let chats = [];

/** @type {number} */
let lastId = 1;

let uploadedFile = null;

/** @type {ParsedFileStrObj|null} */
let parsedFileStrObj = null;

// ===================================================================
// API 호출

/**
 * 사용자의 프롬프트에 대한 채팅 응답을 가져옵니다.
 * @param {string|null} additionalData - JSON 또는 Base64 string
 * @param {boolean|null} hasImage - 이미지가 포함되어 있는지 여부
 * @returns {Promise<string|undefined>} LLM 생성 응답 내용
 */
async function getChatResponse(additionalData = null, hasImage = false) {
  const prompt = chats[chats.length - 2].content;

  let messages;

  if (hasImage) {
    messages = [
      {
        role: "user",
        content: [
          {
            type: "image_url",
            image_url: {
              url: additionalData,
            },
          },
          { type: "text", text: prompt.trim() },
        ],
      },
    ];
  } else if (additionalData) {
    messages = [
      {
        role: "user",
        content: `${additionalData} ${prompt}`.trim(),
      },
    ];
  } else {
    messages = chats.map((chat) => {
      return {
        role: chat.role,
        content: chat.content,
      };
    });

    // 아직 로딩중인 맨 마지막 메세지 삭제
    messages.pop();
  }

  try {
    const response = await axios.post(`${SERVER_URL}/chat/completions/`, {
      messages: messages,
    });
    return response.data.content;
  } catch (error) {
    console.error(error);
  }
}

/**
 * 프롬프트의 내용이 적절한지 가드레일을 통해 확인합니다.
 * @param {string} prompt - 검사할 사용자 입력 메시지
 * @returns {Promise<boolean>} 적절하면 true, 부적절할 경우 서버에서 500번 반환하므로 false 반환
 */
async function getIsAppropriate(prompt) {
  try {
    const response = await axios.post(`${SERVER_URL}/chat/guardrail/`, {
      prompt: prompt,
    });
    return response.data.is_appropriate;
  } catch (error) {
    if (error.status === 500) {
      return false;
    }
  }
}

/**
 * 질문과 답변 쌍에 대한 채팅 품질 점수를 가져옵니다.
 * @param {string} answer - 시스템 응답
 * @param {string|null} additionalData - JSON 또는 Base64 string
 * @param {boolean|null} hasImage - 이미지가 포함되어 있는지 여부
 * @returns {Promise<Object|undefined>} 평가 점수와 이유
 */
async function getChatScore(additionalData = null, hasImage = false) {
  const prompt = chats[chats.length - 2].content;
  const answer = chats[chats.length - 1].content;

  let messages;

  if (hasImage) {
    messages = [
      {
        role: "user",
        content: [
          {
            type: "image_url",
            image_url: {
              url: additionalData,
            },
          },
          { type: "text", text: prompt.trim() },
        ],
      },
      {
        role: "assistant",
        content: answer.trim(),
      },
    ];
  } else {
    messages = [
      {
        role: "user",
        content: `${additionalData || ""} ${prompt}`.trim(),
      },
      {
        role: "assistant",
        content: answer.trim(),
      },
    ];
  }

  const copiedChats = chats.map((chat) => chat);
  copiedChats.pop();
  copiedChats.pop();

  const combinedMessages = [...copiedChats, ...messages];

  try {
    const response = await axios.post(`${SERVER_URL}/chat/score/`, {
      messages: combinedMessages,
      answer: answer,
    });
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

/**
 * 프롬프트를 기반으로 생성된 이미지의 URL을 가져옵니다.
 * @param {string} prompt - 이미지 생성용 묘사 문구
 * @returns {Promise<string|undefined>} 생성된 이미지의 URL
 */
async function getImageGenerationUrl(prompt) {
  try {
    const response = await axios.post(`${SERVER_URL}/images/generations/`, {
      prompt: prompt,
    });
    return response.data.url;
  } catch (error) {
    console.error(error);
  }
}

/**
 * 생성된 이미지 URL이 질문 의도에 부합하는지 점수를 가져옵니다.
 * @param {string} question - 이미지 생성을 요청한 원본 질문
 * @param {string} imageUrl - 생성된 이미지의 URL
 * @returns {Promise<Object|undefined>} 이미지 품질 및 적합성 점수와 이유
 */
async function getImageGenerationScore(question, imageUrl) {
  try {
    const response = await axios.post(`${SERVER_URL}/images/score/url/`, {
      question: question,
      image_url: imageUrl,
    });

    return response.data;
  } catch (error) {
    console.error(error);
  }
}

/**
 * 프롬프트 내용에 따라 적절한 서비스 경로(Route)를 결정합니다.
 * @param {string} prompt - 사용자 입력 메시지
 * @returns {Promise<string|undefined>} 결정된 서비스 라우트 경로
 */
async function getRoute(prompt) {
  try {
    const response = await axios.post(`${SERVER_URL}/decide-route/`, {
      prompt: prompt,
    });
    return response.data.route;
  } catch (error) {
    console.error(error);
  }
}

// ===================================================================
// 유틸 함수

/**
 * 채팅 컨테이너의 스크롤을 최하단으로 부드럽게 이동시킵니다.
 * 마지막 자식 요소를 기준으로 스크롤 위치를 조정합니다.
 * @returns {void}
 */
function scrollToBottom() {
  const lastMessage = chatUl.lastElementChild;
  if (lastMessage) {
    lastMessage.scrollIntoView({ behavior: "smooth", block: "end" });
  }
}

// ===================================================================
// 각 상황에 대한 함수

let chatLis = "";

/**
 * 메인 화면 레이아웃을 채팅 페이지 형식으로 전환합니다.
 * 클래스 교체 및 내부 요소들의 스타일(디스플레이, 패딩, 플렉스 비율 등)을 수정합니다.
 * * @returns {void}
 */
function changePageToChat() {
  chatMain.classList.replace("first-page", "chat-page");
  chatMain.querySelector(".chat-title").style.display = "none";
  chatMain.querySelector(".chat-description").style.display = "none";
  chatMain.style.padding = "20px";
  chatMain.querySelector(".chat-input-wrapper").style.marginTop = "0px";
  chatUl.style.display = "block";
  chatUl.style.flex = "8";
  chatInput.style.flex = "2";
  chatMain.querySelector(
    ".chat-input-container > .file-add-btn-wrapper",
  ).style.bottom = "47%";
}

/**
 * 사용자 질문을 처리하여 적절성 검사, 라우팅, 응답 생성 및 점수 평가를 수행하고 UI를 업데이트합니다.
 * @param {string} userQuestion - 사용자가 입력한 질문 텍스트
 * @param {string|null} additionalData - JSON 또는 Base64 string
 * @param {boolean|null} hasImage - 이미지가 포함되어 있는지 여부
 * @returns {Promise<void>}
 */
async function handleChat(
  userQuestion,
  additionalData = null,
  hasImage = false,
) {
  const file = uploadedFile;

  removeFile();

  // 최초 화면일 경우
  if (chatMain.classList.contains("first-page")) {
    changePageToChat();
  }

  if (chatLis) {
    chatUl.innerHTML = chatLis;
  }

  let additionalTag = "";
  if (file) {
    if (file.type === "image/jpeg" || file.type === "image/png") {
      const tempImageURLForBrowser = URL.createObjectURL(file);

      chats.push({
        id: ++lastId,
        role: "user",
        content: userQuestion,
      });

      additionalTag = `
          <div class="img-wrapper">
            <img src="${tempImageURLForBrowser}" alt="이미지" height="200" />
          </div>
        `;
    } else if (file.type === "application/json") {
      const text = await file.text();
      const jsonObj = JSON.parse(text);
      const jsonStr = JSON.stringify(jsonObj);

      chats.push({
        id: ++lastId,
        role: "user",
        content: jsonStr + userQuestion,
      });

      additionalTag = `<pre>${jsonStr}</pre>`;
    }
  } else {
    chats.push({
      id: ++lastId,
      role: "user",
      content: userQuestion,
    });
  }

  chatLis += `
      <li class="chat-li user-li">
        ${additionalTag}
        <div class="chat-content user">${userQuestion}</div>
      </li>
    `;

  chats.push({
    id: ++lastId,
    role: "assistant",
    content: "부적절한 질문인지 판단중...",
  });

  chatLis += `
      <li class="chat-li assistant-li">
        <div class="loader"></div>
        <div class="chat-content assistant">부적절한 질문인지 판단중...</div>
      </li>
    `;

  chatUl.innerHTML = chatLis;

  chatInput.disabled = "true";

  const lastLi = chatUl.querySelector("li:last-child");
  const lastTextEl = lastLi.querySelector(".assistant");
  const loader = lastLi.querySelector(".loader");

  scrollToBottom();

  const isAppropriate = await getIsAppropriate(userQuestion);
  if (!isAppropriate) {
    loader.remove();
    lastTextEl.textContent = "적절한 질문이 아닙니다.";
    chats[chats.length - 1].content = "적절한 질문이 아닙니다.";
    chatInput.disabled = "";
    chatLis = chatUl.innerHTML;
    return;
  }

  lastTextEl.textContent = "질문의 종류 파악중...";

  const route = await getRoute(userQuestion);

  lastTextEl.textContent = "답변 생성중...";

  if (route === "/chat/completions") {
    const content = await getChatResponse(additionalData, hasImage);

    // 받아온 답변을 배열에 등록
    chats[chats.length - 1].content = content;

    lastTextEl.textContent = "답변의 점수 계산중...";

    const result = await getChatScore(additionalData, hasImage);

    const score = result.score;
    const reason = result.reason;

    lastTextEl.textContent =
      content +
      "\n\n" +
      `질문에 대한 답변 점수: ${score}/100 점` +
      "\n" +
      `이유: ${reason}`;
  } else if (route === "/images/generations") {
    const imageUrl = await getImageGenerationUrl(userQuestion);
    chats[chats.length - 1].content =
      "(답변 이미지. LLM 성능 향상을 위해 message 엔 생략. 답변 점수 계산 시 감안할 것)";
    lastTextEl.textContent = "이미지 점수 계산중...";
    const result = await getImageGenerationScore(userQuestion, imageUrl);

    const score = result.score;
    const reason = result.reason;

    const imgTag = `
      <div class="img-wrapper">
        <img src="${imageUrl}" alt="이미지" height="200" />
      </div>
    `;
    lastLi.insertAdjacentHTML("afterbegin", imgTag);
    lastTextEl.textContent =
      `질문에 대한 답변 이미지 점수: ${score}/100 점` +
      "\n" +
      `이유: ${reason}`;
  }

  scrollToBottom();

  loader.remove();
  chatInput.disabled = "";
  chatLis = chatUl.innerHTML;
}

/**
 * 현재 업로드된 파일 상태를 초기화하고 화면에서 파일 칩 UI를 제거합니다.
 * @returns {void}
 */
function removeFile() {
  uploadedFile = null;
  filePreviewContainer.innerHTML = "";
  parsedFileStrObj = null;
}

/**
 * 선택된 파일의 이름을 화면에 표시하는 파일 칩(Chip) UI를 렌더링합니다.
 * @param {string} name - 표시할 파일의 이름
 * @returns {void}
 */
function renderFileChip(name) {
  filePreviewContainer.innerHTML = `
      <div class="file-chip">
        <span>${name}</span>
        <span class="remove-btn" onclick="removeFile()">X</span>
      </div>
    `;
}

/**
 * 전달받은 파일을 검증하고 확장자에 따라 JSON 문자열 또는 Base64 이미지를 반환합니다.
 * @param {File} file - 처리할 파일 객체
 * @returns {Promise<{additionalData: string, hasImage: boolean} | undefined>}
 * - 성공 시 파일 데이터 객체를 반환하며, 유효하지 않거나 에러 발생 시 undefined를 반환합니다.
 */
async function handleFile(file) {
  // 답변중이라면 작동 안함
  if (chatInput.disabled === true) {
    return;
  }

  // 지원하는 확장자 목록 (소문자로 비교)
  const allowedExtensions = [".json", ".png", ".jpg", ".jpeg"];
  const fileName = file.name.toLowerCase(); // 대소문자 구분 방지
  const isValid = allowedExtensions.some((ext) => fileName.endsWith(ext));

  if (!isValid) {
    alert("json, png, jpeg 파일만 지원합니다.");
    return;
  }

  uploadedFile = file;
  renderFileChip(file.name);

  // 파일 확장자 추출 및 저장
  const fileExtension = fileName.split(".").pop();

  if (fileExtension === "json") {
    const text = await file.text();

    try {
      const jsonObj = JSON.parse(text);
      const jsonStr = JSON.stringify(jsonObj);
      return {
        additionalData: jsonStr,
        hasImage: false,
      };
    } catch (error) {
      alert("파일에 기록된 내용이 올바른 json 이 아닙니다.");
      removeFile();
      return;
    }
  } else if (
    fileExtension === "jpeg" ||
    fileExtension === "jpg" ||
    fileExtension === "png"
  ) {
    // 파일을 Base64로 변환하는 Promise 생성
    const base64String = await new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file); // 파일을 Data URL(Base64)로 읽기 시작
      reader.onload = () => resolve(reader.result); // 읽기 완료 시 결과 반환
      reader.onerror = (error) => reject(error);
    });

    return {
      additionalData: base64String, // "사진" 대신 Base64 문자열 할당
      hasImage: true,
    };
  }
}

// ============================================================================
// 채팅창 엔터 이벤트리스너

chatInput.addEventListener("keypress", async (e) => {
  if (e.key === "Enter" && chatInput.value.trim()) {
    const userQuestion = chatInput.value.trim();
    chatInput.value = "";
    if (parsedFileStrObj) {
      await handleChat(
        userQuestion,
        parsedFileStrObj.additionalData,
        parsedFileStrObj.hasImage,
      );
    } else {
      await handleChat(userQuestion);
    }
  }
});

// ============================================================================
// 파일 추가 버튼 이벤트 리스너

fileAddBtn.addEventListener("click", () => {
  fileInput.click();
});

fileInput.addEventListener("change", async (e) => {
  removeFile();
  const selectedFiles = e.target.files;

  if (selectedFiles.length > 0) {
    const file = selectedFiles[0];
    parsedFileStrObj = await handleFile(file);
  }
});

// ============================================================================
// 드래그 앤 드롭 관련 이벤트 리스너

// 브라우저의 기본 드롭 동작(파일 열기)을 방지
["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
  chatMain.addEventListener(
    eventName,
    (e) => {
      e.preventDefault();
      e.stopPropagation();
    },
    false,
  );
});

// 드래그해서 영역 위로 올라왔을 때 스타일 적용
["dragenter", "dragover"].forEach((eventName) => {
  chatMain.addEventListener(
    eventName,
    () => {
      chatMain.classList.add("drag-over"); // 클래스 추가
    },
    false,
  );
});

// 영역을 벗어나거나 파일을 드롭했을 때 스타일 제거
["dragleave", "drop"].forEach((eventName) => {
  chatMain.addEventListener(
    eventName,
    () => {
      chatMain.classList.remove("drag-over"); // 클래스 제거
    },
    false,
  );
});

// 파일 드롭 시 처리 로직
chatMain.addEventListener("drop", async (e) => {
  removeFile();
  const files = e.dataTransfer.files;
  if (files.length > 0) {
    const file = files[0];
    parsedFileStrObj = await handleFile(file);
  }
});
