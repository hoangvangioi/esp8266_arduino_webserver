import React from 'react';
import { NavLink } from "react-router-dom";


const Sidebar = () => {

    return (
        <aside className="aside is-placed-left is-expanded">
            <div className="aside-tools">
                <div>
                    <b className="font-black">IOT </b>App
                </div>
            </div>
            <div className="menu is-menu-main">
                <p className="menu-label"></p>
                <ul className="menu-list">
                    <li>
                        <NavLink to="/">
                            <span className="icon"><i className="mdi mdi-monitor-dashboard mdi-24px"></i></span>
                            <span className="menu-item-label">Dashboard</span>
                        </NavLink>
                    </li>
                </ul>
                <p className="menu-label"></p>

                <ul className="menu-list">
                    <li>
                        <NavLink to="/temperature">
                            <span className="icon">
                                <i className="mdi mdi-thermometer mdi-24px"></i>
                            </span>
                            <span className="menu-item-label">Temperature</span>
                        </NavLink>
                    </li>
                </ul>
                <p className="menu-label"></p>

                <ul className="menu-list">
                    <li>
                        <NavLink to="/humidity">
                            <span className="icon"><i className="mdi mdi-cloud-percent-outline mdi-24px"></i></span>
                            <span className="menu-item-label">Humidity</span>
                        </NavLink>
                    </li>
                </ul>
                <p className="menu-label"></p>

                <ul className="menu-list">
                    <li>
                        <NavLink to="/light">
                            <span className="icon"><i className="mdi mdi-brightness-4 mdi-24px"></i></span>
                            <span className="menu-item-label">Light</span>
                        </NavLink>
                    </li>
                </ul>
                <p className="menu-label"></p>

                <ul className="menu-list">
                    <li>
                        <NavLink to="/sound">
                            <span className="icon"><i className="mdi mdi-volume-high mdi-24px"></i></span>
                            <span className="menu-item-label">Sound</span>
                        </NavLink>
                    </li>
                </ul>
                <p className="menu-label"></p>

                <ul className="menu-list">
                    <li>
                        <NavLink to="/waterlevel">
                            <span className="icon"><i className="mdi mdi-water mdi-24px"></i></span>
                            <span className="menu-item-label">Water level</span>
                        </NavLink>
                    </li>
                </ul>
            </div>
        </aside>
    );
};

export default Sidebar;