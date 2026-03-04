import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const resources = {
  en: {
    translation: {
      "Welcome": "Welcome to Lifetime Financial Consulting AI",
      "Login": "Login",
      "Signup": "Sign Up",
      "Email": "Email",
      "Password": "Password",
      "Submit": "Submit",
      "Chat": "Chat",
      "Type_a_message": "Type a message...",
      "Send": "Send",
      "Select_Provider": "Select AI Provider",
      "Logout": "Logout",
      "Language": "Language"
    }
  },
  "zh-TW": {
    translation: {
      "Welcome": "歡迎使用終生財務諮詢 AI",
      "Login": "登入",
      "Signup": "註冊",
      "Email": "電子郵件",
      "Password": "密碼",
      "Submit": "送出",
      "Chat": "聊天",
      "Type_a_message": "輸入訊息...",
      "Send": "發送",
      "Select_Provider": "選擇 AI 供應商",
      "Logout": "登出",
      "Language": "語言"
    }
  }
};

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: "en",
    fallbackLng: "en",
    interpolation: {
      escapeValue: false
    }
  });

export default i18n;
