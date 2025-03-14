import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000'; // Passe die URL an deine API an

export const getTuttiContent = async () => {
  const response = await axios.get(`${API_BASE_URL}/tutti-content`);
  return response.data;
};