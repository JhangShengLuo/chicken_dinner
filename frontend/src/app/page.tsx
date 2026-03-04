'use client';

import React, { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { useAppStore } from '@/lib/store';
import { api } from '@/lib/api';
import Navbar from '@/components/Navbar';
import '@/i18n/config';

export default function Home() {
  const { t } = useTranslation();
  const { token, setToken, provider, language } = useAppStore();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLogin, setIsLogin] = useState(true);
  const [error, setError] = useState('');

  const [messages, setMessages] = useState<{role: string, content: string}[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Component mounted
  }, []);

  const handleAuth = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    try {
      if (isLogin) {
        const formData = new URLSearchParams();
        formData.append('username', email);
        formData.append('password', password);
        const res = await api.post('/token', formData, {
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        });
        setToken(res.data.access_token);
      } else {
        await api.post('/register', { email, password });
        setIsLogin(true);
        setError('Registration successful. Please login.');
      }
    } catch (err: any) {
      setError(err.response?.data?.detail || 'An error occurred');
    }
  };

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || !token) return;

    const userMsg = input;
    setMessages(prev => [...prev, { role: 'user', content: userMsg }]);
    setInput('');
    setLoading(true);

    try {
      const res = await api.post('/api/chat/message', {
        message: userMsg,
        provider: provider,
        language: language === 'zh-TW' ? '繁體中文' : 'English',
        history: []
      });
      setMessages(prev => [...prev, { role: 'assistant', content: res.data.reply }]);
    } catch (err: any) {
      console.error(err);
      setMessages(prev => [...prev, { role: 'assistant', content: 'Error communicating with AI.' }]);
    } finally {
      setLoading(false);
    }
  };

  if (!token) {
    return (
      <div className="min-h-screen bg-gray-100">
        <Navbar />
        <div className="flex flex-col items-center justify-center pt-20">
          <h1 className="text-3xl font-bold mb-8 text-blue-600">{t('Welcome')}</h1>
          <form onSubmit={handleAuth} className="bg-white p-8 rounded shadow-md w-96">
            <h2 className="text-2xl mb-4 text-center text-gray-800">{isLogin ? t('Login') : t('Signup')}</h2>
            {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
            <input
              type="email"
              placeholder={t('Email')}
              className="w-full border p-2 mb-4 rounded text-black"
              value={email}
              onChange={e => setEmail(e.target.value)}
              required
            />
            <input
              type="password"
              placeholder={t('Password')}
              className="w-full border p-2 mb-4 rounded text-black"
              value={password}
              onChange={e => setPassword(e.target.value)}
              required
            />
            <button type="submit" className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700">
              {t('Submit')}
            </button>
            <p className="mt-4 text-center text-sm cursor-pointer text-blue-500 hover:underline" onClick={() => setIsLogin(!isLogin)}>
              {isLogin ? "Need an account? Sign up" : "Already have an account? Login"}
            </p>
          </form>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <Navbar />
      <div className="flex-1 flex flex-col max-w-4xl w-full mx-auto p-4">
        <div className="flex-1 bg-white border rounded-lg shadow-sm p-4 overflow-y-auto mb-4 flex flex-col space-y-4">
          {messages.length === 0 && (
            <div className="text-center text-gray-500 my-auto">{t('Welcome')}! Ask me about your financial goals, affordability, or life insurance.</div>
          )}
          {messages.map((msg, i) => (
            <div key={i} className={`p-3 rounded-lg max-w-[80%] whitespace-pre-wrap ${msg.role === 'user' ? 'bg-blue-100 text-blue-900 self-end' : 'bg-gray-100 text-gray-800 self-start'}`}>
              <span className="font-bold text-xs uppercase block mb-1 text-gray-500">{msg.role}</span>
              {msg.content}
            </div>
          ))}
          {loading && <div className="text-gray-500 text-sm italic">AI is thinking...</div>}
        </div>

        <form onSubmit={handleSend} className="flex gap-2">
          <input
            type="text"
            className="flex-1 border p-3 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
            placeholder={t('Type_a_message')}
            value={input}
            onChange={e => setInput(e.target.value)}
            disabled={loading}
          />
          <button
            type="submit"
            className="bg-blue-600 text-white px-6 py-3 rounded-lg shadow-sm hover:bg-blue-700 disabled:opacity-50"
            disabled={loading}
          >
            {t('Send')}
          </button>
        </form>
      </div>
    </div>
  );
}
