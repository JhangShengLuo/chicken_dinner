'use client';

import React, { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { useAppStore } from '@/lib/store';
import { api } from '@/lib/api';

export default function Navbar() {
  const { t, i18n } = useTranslation();
  const { language, setLanguage, provider, setProvider, token, setToken } = useAppStore();
  const [providers, setProviders] = useState<string[]>([]);

  useEffect(() => {
    i18n.changeLanguage(language);

    api.get('/api/providers')
      .then(res => setProviders(res.data.providers))
      .catch(console.error);
  }, [language, i18n]);

  const handleLangChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setLanguage(e.target.value);
  };

  const handleLogout = () => {
    setToken(null);
  };

  return (
    <nav className="flex items-center justify-between p-4 bg-blue-600 text-white shadow-md">
      <div className="text-xl font-bold">LFC AI</div>

      <div className="flex items-center space-x-4">
        {token && (
          <select
            value={provider}
            onChange={(e) => setProvider(e.target.value)}
            className="text-black p-1 rounded"
          >
            <option disabled>{t('Select_Provider')}</option>
            {providers.map(p => <option key={p} value={p}>{p}</option>)}
          </select>
        )}

        <select
          value={language}
          onChange={handleLangChange}
          className="text-black p-1 rounded"
        >
          <option value="en">English</option>
          <option value="zh-TW">繁體中文</option>
        </select>

        {token && (
          <button onClick={handleLogout} className="bg-red-500 px-3 py-1 rounded hover:bg-red-700">
            {t('Logout')}
          </button>
        )}
      </div>
    </nav>
  );
}
