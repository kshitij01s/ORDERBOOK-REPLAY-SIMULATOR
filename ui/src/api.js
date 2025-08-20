import axios from 'axios';

const API = "http://localhost:8000";

export const getOrderBook = async () => {
  const res = await axios.get(`${API}/book`);
  return res.data;
};
