// src/App.tsx
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import LoginPage from "./pages/login";
import DashboardPage from "./pages/Dashboard";

function App() {
  const token = localStorage.getItem("kapos_access");

  return (
    <BrowserRouter>
      <Routes>
        {/* Login */}
        <Route path="/login" element={<LoginPage />} />

        {/* Dashboard protegido (solo si hay token) */}
        <Route
          path="/dashboard"
          element={
            token ? <DashboardPage /> : <Navigate to="/login" replace />
          }
        />

        {/* Redirección por defecto */}
        <Route
          path="*"
          element={
            token ? (
              <Navigate to="/dashboard" replace />
            ) : (
              <Navigate to="/login" replace />
            )
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
