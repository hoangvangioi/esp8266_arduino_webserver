import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css'
// eslint-disable-next-line
import { Chart } from "chart.js/auto";


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <App/>
    </React.StrictMode>
);