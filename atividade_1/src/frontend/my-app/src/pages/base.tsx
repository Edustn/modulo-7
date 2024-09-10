import "../app/globals.css";

export default function Base() {
    return (
        <div className="bg-amber-50 min-h-screen flex flex-col items-center justify-center">
            <div>
                <p className="normal-case text-slate-950 text-5xl font-bold mb-8">
                    Bem-Vindo! Preveja seus Bitcoins
                </p>
                <div className="flex space-x-4 text-center justify-center">
                    <button className="text-slate-950 text-2xl text-center font-bold bg-amber-200 rounded-lg p-2 w-auto">
                        Base Treinada
                    </button>
                    <button className="text-slate-950 text-2xl text-center font-bold bg-amber-200 rounded-lg p-2 w-auto">
                        Treinar
                    </button>
                </div>
            </div>
        </div>
    );
}
