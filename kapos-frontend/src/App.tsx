import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import LoginPage from "./pages/Login";
import DashboardPage from "./pages/Dashboard";

export default function App() {
  const isLoggedIn = Boolean(localStorage.getItem("kapos_access"));

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />

        <Route
          path="/dashboard"
          element={isLoggedIn ? <DashboardPage /> : <Navigate to="/login" />}
        />

        {/* Próximas rutas */}
        <Route
          path="/clientes"
          element={isLoggedIn ? <div>Clientes</div> : <Navigate to="/login" />}
        />
        <Route
          path="/planes"
          element={isLoggedIn ? <div>Planes</div> : <Navigate to="/login" />}
        />
        <Route
          path="/suscripciones"
          element={isLoggedIn ? <div>Suscripciones</div> : <Navigate to="/login" />}
        />

        <Route path="*" element={<Navigate to="/dashboard" />} />
      </Routes>
    </BrowserRouter>
  );
}
