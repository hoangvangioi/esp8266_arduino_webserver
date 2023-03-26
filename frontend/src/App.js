import React from 'react';
import { BrowserRouter } from 'react-router-dom'
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import MainPage from "./components/MainPage";


function App() {
	return (
        <BrowserRouter>
            <Header/>
            <Sidebar/>
            <MainPage/>
        </BrowserRouter>
	);
}
export default App;