"use client";

import Link from 'next/link';
import { useRouter } from 'next/navigation';
import axios from "axios";


export default function Home() {


  const router = useRouter();

  const handleBaseTreinadaClick = async () => {
    try {
      
      const response = await axios.get('http://localhost:8000/executar/modelo');
      
      console.log('Resposta da API:', response.data);

      router.push('/results')

    } catch (error) {
      console.error('Erro na rota /executar/modelo', error)
    }

  }

  return (
    <div className="bg-amber-50 min-h-screen flex flex-col items-center justify-center">
      <div>
        <p className="normal-case text-slate-950 text-5xl font-bold mb-8">
          Bem-Vindo! Preveja seus Bitcoins
        </p>
        <div className="flex space-x-4 text-center justify-center">

          <button onClick={handleBaseTreinadaClick} className="text-slate-950 text-2xl text-center font-bold bg-amber-200 rounded-lg p-2 w-auto">
            Base Treinada
          </button>
          <Link href='insereBase'>
            <button className="text-slate-950 text-2xl text-center font-bold bg-amber-200 rounded-lg p-2 w-auto">
              Treinar
            </button>
          </Link>

          <Link href='grafico'>
            <button className="text-slate-950 text-2xl text-center font-bold bg-amber-200 rounded-lg p-2 w-auto">
              Gráfico
            </button>
          </Link>


        </div>
      </div>
    </div>
  );
}
