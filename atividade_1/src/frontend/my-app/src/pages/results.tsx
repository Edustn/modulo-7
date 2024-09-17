import { useEffect, useState } from "react";
import "../app/globals.css";
import axios from "axios"

export default function Results() {
    const [message, setMessage] = useState("");  // Para armazenar a mensagem retornada pela API
    const [data, setData] = useState(null);      // Para armazenar o resultado[0]

    // Função para buscar os dados da API FastAPI
    useEffect(() => {
        async function fetchResults() {
            try {
                const response = await axios.get("http://127.0.0.1:8000/executar/modelo"); // Substitua pelo seu endpoint
                const result = await response.data;

                // O resultado será um array contendo [message, resultado[0]]
                setMessage(result[0]);
                setData(result[1]);
            } catch (error) {
                console.error("Erro ao buscar resultados:", error);
            }
        }

        fetchResults();
    }, []); // O array vazio [] significa que o efeito será executado apenas uma vez após a renderização

    return (
        <div className="bg-amber-50 min-h-screen flex flex-col items-center justify-center">
            <h1 className="text-black text-4xl font-bold">Seus resultados foram:</h1>
            <p className="text-black text-xl">{message}</p>

            {data && <p className="text-black text-lg mt-4">Melhores dias para comprar BitCoin segundo essa base são: {data}</p>}
        </div>
    );
}
