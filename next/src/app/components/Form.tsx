import React from 'react';
import styles from '../styles/styles';

interface FormProps {
  handleSubmit: (e: React.FormEvent) => void;
  name: string;
  setName: (name: string) => void;
  selectedTable: string;
  setSelectedTable: (table: string) => void;
  tables: string[];
}

const Form: React.FC<FormProps> = ({ handleSubmit, name, setName, selectedTable, setSelectedTable, tables }) => {
  return (
    <form onSubmit={handleSubmit} className={styles.form}>
      <label htmlFor="table-select" className={styles.label}>
        Select a Table
      </label>
      <select
        id="table-select"
        value={selectedTable}
        onChange={(e) => setSelectedTable(e.target.value)}
        className={styles.select}
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
        className={styles.input}
      />
      <button type="submit" className={styles.button}>
        Submit
      </button>
    </form>
  );
};

export default Form;
