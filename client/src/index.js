import React from "react";
import ReactDOM from "react-dom";
import App from "./components/App";
import { BrowserRouter } from "react-router-dom";
import { createRoot } from "react-dom/client";
import "./index.css";
import 'semantic-ui-css/semantic.min.css'

const root = createRoot(document.getElementById("root"));

root.render(
    <BrowserRouter>
        <App />
    </BrowserRouter>
    );