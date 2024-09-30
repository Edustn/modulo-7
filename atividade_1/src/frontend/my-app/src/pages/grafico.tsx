import React, { useEffect, useState } from 'react';
import axios from 'axios';
import "../app/globals.css";

const ImageComponent = () => {
  const [imageSrc, setImageSrc] = useState<string | null>(null); // Tipagem explícita para string ou null

  useEffect(() => {
    const fetchImage = async () => {
      try {
        // Faz a requisição para o backend FastAPI para pegar a imagem
        const response = await axios.get('http://localhost:8000/dash', {
          responseType: 'blob', // Define o tipo da resposta como blob (para arquivos de mídia)
        });

        // Cria um URL para o blob da imagem recebida
        const imageUrl = URL.createObjectURL(response.data);
        setImageSrc(imageUrl); // Define a URL da imagem
      } catch (error) {
        console.error('Erro ao carregar a imagem:', error);
      }
    };

    fetchImage();
  }, []);

  return (
    <div>
      {imageSrc ? (
        <img src={imageSrc} alt="Volatilidade GARCH" />
      ) : (
        <p>Carregando imagem...</p>
      )}
    </div>
  );
};

export default ImageComponent;
