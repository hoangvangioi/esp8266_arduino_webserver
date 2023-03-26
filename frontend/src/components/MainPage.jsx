import React from "react";
import { Routes, Route } from 'react-router-dom'
import Home from '../pages/Home'
import Temperature from '../pages/Temperature'
import Humidity from '../pages/Humidity'
import Light from '../pages/Light'
import Sound from '../pages/Sound'
import WaterLevel from '../pages/WaterLevel'


const MainPage = () => {
    
    return (
        <section className="section main-section">
            <div className="card mb-6">
                <header className="card-header">
                    <p className="card-header-title">
                        <span className="icon"><i className="mdi mdi-finance"></i></span>Performance
                    </p>
                </header>
                <div className="card-content">
                    <div className="chart-area">
                        <div className="h-full">
                            <Routes>
                                <Route path='/' element={<Home />} />
                                <Route path='/temperature' element={<Temperature />} />
                                <Route path='/humidity' element={<Humidity />} />
                                <Route path='/light' element={<Light />} />
                                <Route path='/sound' element={<Sound />} />
                                <Route path='/waterlevel' element={<WaterLevel />} />
                            </Routes>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default MainPage;