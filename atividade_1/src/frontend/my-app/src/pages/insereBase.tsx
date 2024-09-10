import { useState } from "react";
import "../app/globals.css";

export default function InsereBase() {
  const [file, setFile] = useState(null);

  const handleFileChange = async(e) => {
    const uploadedFile = e.target.files[0];
    setFile(uploadedFile);
    console.log("Arquivo selecionado:", uploadedFile);
  };

  const handleButtonClick = () => {
    // Quando o botão for clicado, simula o clique no input file escondido
    document.getElementById("fileInput").click();
  };

  return (
    <div className="bg-amber-50 min-h-screen flex flex-col items-center justify-center">
      <input
        id="fileInput"
        type="file"
        accept=".csv"
        style={{ display: "none" }} // Esconde o input de arquivo
        onChange={handleFileChange}
      />
      <button
        className="text-slate-950 text-2xl text-center font-bold bg-amber-200 rounded-lg p-2 w-auto"
        onClick={handleButtonClick}>
        Enviar tabela
      </button>

      {file && <p className="text-black mt-4">Arquivo selecionado: {file.name}</p>}
    </div>
  );
}
