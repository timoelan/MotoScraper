import axios from 'axios';
import { Motorrad } from '../components/Motorrad';

const API_BASE_URL = 'http://localhost:8000'; // Passe die URL an deine API an

export const getTuttiContent = async () => {
  const response = await axios.get<Motorrad[]>(`${API_BASE_URL}/tutti-content`);



  return response.data;
};

const res = axios.get(`${API_BASE_URL}/tutti-content`)
res.then((data) => {

})