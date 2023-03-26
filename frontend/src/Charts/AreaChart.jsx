import React, { useState, useEffect } from 'react'
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';

import { Line } from 'react-chartjs-2';
import axios from "axios";

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);


const AreaChart = ({apiUrl, value_1, value_2}) => {
    
    const [labelschart, setLabelsChart] = useState([]);
    const [datachart, setDataChart] = useState([]);
    
    useEffect(() => {
        const fetchDatas = async () => {
        try {
            const response = await axios.get(`${process.env.REACT_APP_API_URL}/${apiUrl}`);
            const result = {
                [value_1]: response.data.map((item) => item[value_1]),
                [value_2]: response.data.map((item) => item[value_2]),
            };
            setLabelsChart(result[value_2]);
            setDataChart(result[value_1]);
        } catch (error) {
            console.log(error);
        }
        };
        fetchDatas();
    }, [apiUrl, value_1, value_2]);

    const labelschart24 = labelschart.slice(-24);
    const datachart24 = datachart.slice(-24);

    const data = {
        labels: labelschart24,
        datasets: [{
            label: `Coins Available`,
            data: datachart24,
            fill: true,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    };

    const options = {
        maintainAspectRatio: false,
            scales: {
        },
        legend: {
            labels: {
                fontSize: 25,
            },
        },
        responsive : true
    }

    return (
        <div>
            <Line
                data={data}
                height={500}
                options={options}
            />
        </div>
    )
}

export default AreaChart