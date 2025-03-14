import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MotorradList from './components/MotorradList';
import MotorradDetail from './components/MotorradDetail';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MotorradList />} />
        <Route path="/motorrad/:id" element={<MotorradDetail />} />
      </Routes>
    </Router>
  );
};

export default App;