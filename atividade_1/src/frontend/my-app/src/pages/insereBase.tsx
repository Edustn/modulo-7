import { useState } from "react";
import "../app/globals.css";

export default function InsereBase() {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    const uploadedFile = e.target.files[0];
    setFile(uploadedFile);
    console.log("Arquivo selecionado:", uploadedFile);
  };

  const handleButtonClick = () => {
    document.getElementById("fileInput").click();
  };  

  const handleUpload = async () => {
    if (!file) {
      alert("Por favor, selecione um arquivo antes de enviar.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/inserirBase", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        alert("Arquivo enviado com sucesso!");
      } else {
        alert("Erro ao enviar o arquivo.");
      }
    } catch (error) {
      console.error("Erro no upload:", error);
    }
  };

  return (
    <div className="bg-amber-50 min-h-screen flex flex-col items-center justify-center">
      <input
        id="fileInput"
        type="file"
        accept=".csv"
        style={{ display: "none" }}
        onChange={handleFileChange}
      />
      <button
        className="text-slate-950 text-2xl text-center font-bold bg-amber-200 rounded-lg p-2 w-auto"
        onClick={handleButtonClick}
      >
        Escolher base
      </button>
      <br />
      <button
        className="text-slate-950 text-2xl text-center font-bold bg-amber-200 rounded-lg p-2 w-auto"
        onClick={handleUpload}
      >
        Enviar base
      </button>

      {file && <p className="text-black mt-4">Arquivo selecionado: {file.name}</p>}
    </div>
  );
}
