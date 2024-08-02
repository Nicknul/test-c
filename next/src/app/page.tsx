'use client';

import { useEffect, useState } from 'react';

interface UserDTO {
  이름: string;
  아이디: string;
  비밀번호: number;
}

export default function Home() {
  const [name, setName] = useState('');
  const [users, setUsers] = useState<UserDTO[]>([]);
  const [error, setError] = useState('');
  const [tables, setTables] = useState<string[]>([]);
  const [selectedTable, setSelectedTable] = useState('');

  useEffect(() => {
    const fetchTables = async () => {
      try {
        const res = await fetch('http://127.0.0.1:8000/tables');
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        const data: string[] = await res.json();
        setTables(data);
        setSelectedTable(data[0] || '');
      } catch (error) {
        setError('Failed to fetch tables');
      }
    };
    fetchTables();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const res = await fetch('http://127.0.0.1:8000/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name }),
      });

      if (!res.ok) {
        throw new Error('Network response was not ok');
      }

      const data: UserDTO[] = await res.json();
      setUsers(data);
      setError('');
    } catch (error) {
      setError('Failed to fetch data');
      setUsers([]);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
        <h1 className="text-2xl font-bold mb-6 text-center">Search User in FastAPI</h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <label htmlFor="table-select" className="block text-sm font-medium text-gray-700">
            Select a Table
          </label>
          <select
            id="table-select"
            value={selectedTable}
            onChange={(e) => setSelectedTable(e.target.value)}
            className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            {tables.map((table) => (
              <option key={table} value={table}>
                {table}
              </option>
            ))}
          </select>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Name"
            required
            className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition duration-300"
          >
            Submit
          </button>
        </form>
        {error && <p className="mt-4 text-center text-red-500">{error}</p>}
        <div className="mt-6">
          {users.length > 0 && (
            <ul className="space-y-2">
              {users.map((user, index) => (
                <li key={index} className="p-4 bg-gray-200 rounded-md">
                  <p>이름: {user.이름}</p>
                  <p>아이디: {user.아이디}</p>
                  <p>비밀번호: {user.비밀번호}</p>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}
