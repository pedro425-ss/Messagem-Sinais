import streamlit as st
import time

st.set_page_config(
    page_title="IA do Destino ❤️",
    page_icon="❤️",
    layout="centered"
)

YOUTUBE_ID = "MxwZ66L9RQI"

st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #ff7eb3 0%, #2b0036 45%, #050008 100%);
    color: white;
}

.card {
    padding: 26px;
    border-radius: 28px;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.25);
    box-shadow: 0 25px 70px rgba(0,0,0,0.35);
    text-align: center;
    margin: 18px 0;
}

.title {
    text-align: center;
    font-size: 44px;
    font-weight: 900;
    letter-spacing: 2px;
    text-shadow: 0 0 14px #ff7eb3, 0 0 30px #ff4f81;
}

.subtitle {
    text-align: center;
    font-size: 20px;
}

.big {
    font-size: 30px;
    font-weight: 800;
    text-align: center;
}

.text {
    font-size: 21px;
    line-height: 1.7;
    text-align: center;
}

.heart {
    font-size: 64px;
    text-align: center;
    animation: pulse 1s infinite;
}

.code {
    font-family: monospace;
    background: rgba(0,0,0,0.35);
    padding: 16px;
    border-radius: 18px;
    text-align: left;
    font-size: 15px;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.22); }
    100% { transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

if "liberado" not in st.session_state:
    st.session_state.liberado = False

st.markdown("<div class='title'>IA DO DESTINO</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Sistema secreto criado para uma pessoa específica.</div>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <p class="text">Para acessar, digite a data que mudou tudo.</p>
</div>
""", unsafe_allow_html=True)

senha = st.text_input("Senha de acesso", placeholder="Ex: 17/04", type="password")

if st.button("Desbloquear sistema"):
    if senha.strip().lower() in ["17/04", "17 de abril", "1704", "17-04"]:
        st.session_state.liberado = True
        st.rerun()
    else:
        st.error("Senha incorreta... dica: foi o dia que tudo começou.")

if st.session_state.liberado:
    st.success("Acesso liberado ❤️")

    st.markdown("### 🎵 Antes de começar")
    st.markdown("Dá play na música e depois inicia a análise ❤️")

    st.markdown(f"""
    <iframe width="100%" height="215"
    src="https://www.youtube.com/embed/{YOUTUBE_ID}"
    title="Sinais - Luan Santana"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
    </iframe>
    """, unsafe_allow_html=True)

    st.markdown("---")

    if st.button("Rodar análise completa"):
        etapas = [
            "Carregando memórias desde 17 de abril...",
            "Detectando primeira conexão...",
            "Analisando conversas que nunca pararam...",
            "Calculando felicidade gerada por você...",
            "Verificando planos de futuro...",
            "Buscando possibilidade de casa, família e filhos...",
            "Processando sentimento verdadeiro...",
            "Resultado encontrado."
        ]

        for etapa in etapas:
            with st.spinner(etapa):
                time.sleep(1.1)
            st.success(etapa)

        st.markdown("<p class='big'>Métricas emocionais</p>", unsafe_allow_html=True)

        metricas = {
            "Felicidade quando falo com você": 99,
            "Vontade de te ver sorrir": 100,
            "Chance de pensar em você do nada": 98,
            "Cuidado que quero ter por você": 100,
            "Futuro que imagino com você": 100,
            "Nível de certeza que você é especial": 100
        }

        for nome, valor in metricas.items():
            st.write(f"**{nome}**")
            st.progress(valor)
            time.sleep(0.45)

        st.markdown("""
        <div class="card">
            <p class="big">Mensagem descriptografada:</p>

            <p class="text">
                Desde o dia <b>17 de abril</b>, alguma coisa mudou.
                Depois daquele dia, a gente não parou mais de se falar...
                e eu sinceramente não queria que parasse.
            </p>

            <p class="text">
                Você me faz sentir feliz, único e importante.
                E eu quero fazer você se sentir assim também:
                amada, cuidada, escolhida e a mulher mais especial do mundo.
            </p>

            <p class="text">
                Eu penso em ser cunhado da sua irmã, genro da sua mãe,
                ter uma casa, filhos e uma vida inteira construída com você.
            </p>

            <p class="big">
                Resultado final: meu coração escolheu você.
            </p>

            <div class="heart">❤️</div>
        </div>
        """, unsafe_allow_html=True)

        st.balloons()

    st.markdown("---")
    st.markdown("<p class='big'>Missão final</p>", unsafe_allow_html=True)

    escolha = st.radio(
        "Você aceita continuar essa história comigo?",
        [
            "Ainda estou pensando...",
            "Sim ❤️",
            "Claro que sim ❤️",
            "Sim, mas você vai ter que me mimar 😌"
        ]
    )

    if escolha == "Sim ❤️":
        st.success("Resposta registrada: você acabou de fazer meu dia melhor. ❤️")
        st.balloons()

    elif escolha == "Claro que sim ❤️":
        st.success("Sistema travou de felicidade. Reinicializando coração... ❤️")
        st.balloons()
        st.snow()

    elif escolha == "Sim, mas você vai ter que me mimar 😌":
        st.success("Contrato aceito. Mimos, carinho e atenção: ativados com sucesso. ❤️")
        st.balloons()

    st.markdown("""
    <div class="card">
        <p class="code">
        if ela == "especial":<br>
        &nbsp;&nbsp;&nbsp;&nbsp;cuidar += infinito<br>
        &nbsp;&nbsp;&nbsp;&nbsp;amar += todos_os_dias<br>
        &nbsp;&nbsp;&nbsp;&nbsp;futuro = "com ela"
        </p>
    </div>
    """, unsafe_allow_html=True)
