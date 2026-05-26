SERVER_URL = "http://localhost:8080/api/v1";

const chatMain = document.querySelector(".chat-main");
const chatInput = document.querySelector(".chat-input");
const chatUl = document.querySelector(".chat-ul");

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

// ===================================================================
// API 호출

/**
 * 사용자의 프롬프트에 대한 채팅 응답을 가져옵니다.
 * @returns {Promise<string|undefined>} LLM 생성 응답 내용
 */
async function getChatResponse() {
  let messages;

  messages = chats.map((chat) => {
    return {
      role: chat.role,
      content: chat.content,
    };
  });

  // 아직 로딩중인 맨 마지막 메세지 삭제
  messages.pop();

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
 * 서버에 텍스트를 전송하여 생성된 TTS(Text-to-Speech) 오디오 데이터를 가져옵니다.
 * @param {string} text - 음성으로 변환할 텍스트 내용
 * @returns {Promise<string|undefined>} 서버에서 반환한 오디오 데이터(base64 등)
 */
async function getTTSResponse(text) {
  try {
    const response = await axios.post(`${SERVER_URL}/generate-speech/`, {
      text: text,
    });
    return response.data.audio_data;
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
  chatMain.style.padding = "20px";
  chatMain.querySelector(".chat-input-wrapper").style.marginTop = "0px";
  chatUl.style.display = "block";
  chatUl.style.flex = "8";
  chatInput.style.flex = "2";
}

/**
 * 사용자 질문을 처리하여 TTS 응답을 생성하고 UI를 업데이트합니다.
 * @param {string} userQuestion - 사용자가 입력한 질문 텍스트
 * @returns {Promise<void>}
 */
async function handleChat(userQuestion) {
  // 최초 화면일 경우
  if (chatMain.classList.contains("first-page")) {
    changePageToChat();
  }

  if (chatLis) {
    chatUl.innerHTML = chatLis;
  }

  chats.push({
    id: ++lastId,
    role: "user",
    content: userQuestion,
  });

  chatLis += `
      <li class="chat-li user-li">
        <div class="chat-content user">${userQuestion}</div>
      </li>
    `;

  chats.push({
    id: ++lastId,
    role: "assistant",
    content: "",
  });

  chatLis += `
      <li class="chat-li assistant-li">
        <div class="loader"></div>
        <div class="chat-content assistant"></div>
      </li>
    `;

  chatUl.innerHTML = chatLis;

  chatInput.disabled = "true";

  const lastLi = chatUl.querySelector("li:last-child");
  const lastEl = lastLi.querySelector(".assistant");
  const loader = lastLi.querySelector(".loader");

  scrollToBottom();

  const content = await getChatResponse();

  // 받아온 답변을 배열에 등록
  chats[chats.length - 1].content = content;

  const audio_data = await getTTSResponse(content);

  lastEl.innerHTML = `
      <div class="audio-wrapper">
        <audio id="myAudio" controls src="data:audio/mp3;base64,${audio_data}"></audio>
      </div>
    `;

  scrollToBottom();

  loader.remove();
  chatInput.disabled = "";
  chatLis = chatUl.innerHTML;
}

// ============================================================================
// 채팅창 엔터 이벤트리스너

chatInput.addEventListener("keypress", async (e) => {
  if (e.key === "Enter" && chatInput.value.trim()) {
    const userQuestion = chatInput.value.trim();
    chatInput.value = "";
    await handleChat(userQuestion);
  }
});

