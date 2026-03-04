import { create } from 'zustand';
import Cookies from 'js-cookie';

interface AppState {
  token: string | null;
  language: string;
  provider: string;
  setToken: (token: string | null) => void;
  setLanguage: (lang: string) => void;
  setProvider: (provider: string) => void;
}

export const useAppStore = create<AppState>((set) => ({
  token: Cookies.get('token') || null,
  language: Cookies.get('language') || 'en',
  provider: 'openai',
  setToken: (token) => {
    if (token) Cookies.set('token', token);
    else Cookies.remove('token');
    set({ token });
  },
  setLanguage: (lang) => {
    Cookies.set('language', lang);
    set({ language: lang });
  },
  setProvider: (provider) => set({ provider }),
}));
