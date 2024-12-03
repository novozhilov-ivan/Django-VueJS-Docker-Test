import axios from "axios";

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api/v1/',  // Базовый URL Django backend
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 3000,
});

axiosInstance.interceptors.response.use(
  response => response,
  error => {
    console.error('API Error:', error);
    return Promise.reject(error);
  }
);

export default axiosInstance;