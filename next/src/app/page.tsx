'use client';

import { useEffect, useState } from 'react';
import DataTable from './components/DataTable';
import Form from './components/Form';
import styles from './styles/styles';

interface UserDTO {
  [key: string]: string | number;
}

export default function Home() {
  const [name, setName] = useState('');
  const [data, setData] = useState<UserDTO[]>([]);
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
      const requestData = { table: selectedTable, name: name || null };
      const res = await fetch('http://127.0.0.1:8000/data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
      });

      if (!res.ok) {
        throw new Error('Network response was not ok');
      }

      const data: UserDTO[] = await res.json();
      setData(data);
      setError('');
    } catch (error) {
      setError('Failed to fetch data');
      setData([]);
    }
  };

  return (
    <div className={styles.mainContainer}>
      <div className={styles.content}>
        <Form
          handleSubmit={handleSubmit}
          name={name}
          setName={setName}
          selectedTable={selectedTable}
          setSelectedTable={setSelectedTable}
          tables={tables}
        />
        {error && <p className={styles.error}>{error}</p>}
      </div>
      <DataTable data={data} />
    </div>
  );
}
