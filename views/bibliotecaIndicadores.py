import streamlit as st
import pandas as pd
import plotly.express as px





def mostrar_graficos_colesterol_4columnas(df):
    """
    Función que muestra 4 gráficos de torta para diferentes grupos de pacientes
    según el número de registros que tengan (1, 2, 3 o 4 registros)
    
    Args:
        df (DataFrame): DataFrame con los datos de pacientes
    """
    # Convertir la columna de marca temporal a datetime
    df['Marca temporal'] = pd.to_datetime(df['Marca temporal'])
    
    # Obtener fechas mínima y máxima para el slider
    min_date = df['Marca temporal'].min().to_pydatetime()
    max_date = df['Marca temporal'].max().to_pydatetime()
    
    # Slider de rango de fechas
    st.sidebar.header("Seleccione el rango de fechas")
    date_range = st.sidebar.slider(
        "Rango de fechas",
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date),
        format="YYYY-MM-DD"
    )
    
    # Filtrar datos por rango de fechas
    mask = (df['Marca temporal'] >= date_range[0]) & (df['Marca temporal'] <= date_range[1])
    filtered_df = df.loc[mask]
    
    # Contar registros por paciente
    patient_counts = filtered_df['Número de documento (sin puntos ni comas)'].value_counts()
    
    # Definir el orden categórico correcto para el colesterol no HDL
    categories = [
        'no-HDL: <100',
        'no-HDL:  >/= 100  - 129',
        'no-HDL:  >/=130  - 159',
        'no-HDL:  >/= 160   - 189',
        '>/=190'
    ]
    
    # Función para crear gráfico de torta
    def create_pie_chart(data, title):
        if not data.empty:
            # Convertir a categoría ordenada
            data['Colesterol no HDL (Fórmula: CT-HDL)'] = pd.Categorical(
                data['Colesterol no HDL (Fórmula: CT-HDL)'],
                categories=categories,
                ordered=True
            )
            
            # Contar valores y ordenarlos según las categorías definidas
            counts = data['Colesterol no HDL (Fórmula: CT-HDL)'].value_counts().reindex(categories)
            
            fig = px.pie(
                counts,
                names=counts.index,
                values=counts.values,
                title=title,
                hole=0.4,
                category_orders={'names': categories}
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')
            return fig
        return None
    
    # Dividir en 4 columnas
    st.header("Distribución de Colesterol no HDL por Grupo")
    col1, col2, col3, col4 = st.columns(4)

        
    # Grupo 1: pacientes con exactamente 1 registro
    with col1:
        group1_ids = patient_counts[patient_counts == 1].index
        group1_df = filtered_df[filtered_df['Número de documento (sin puntos ni comas)'].isin(group1_ids)]
        fig1 = create_pie_chart(group1_df, "Pacientes con 1 registro")
        if fig1:
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.write("No hay pacientes con 1 registro")
    
    # Grupo 2: pacientes con exactamente 2 registros (segundo registro)
    with col2:
        group2_ids = patient_counts[patient_counts == 2].index
        group2_df = filtered_df[filtered_df['Número de documento (sin puntos ni comas)'].isin(group2_ids)]
        # Ordenar y tomar el segundo registro de cada paciente
        group2_df = group2_df.sort_values(['Número de documento (sin puntos ni comas)', 'Marca temporal'])
        group2_df = group2_df.groupby('Número de documento (sin puntos ni comas)').nth(1).reset_index()
        fig2 = create_pie_chart(group2_df, "Segundo registro (2 registros)")
        if fig2:
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.write("No hay pacientes con 2 registros")
    
    # Grupo 3: pacientes con exactamente 3 registros (tercer registro)
    with col3:
        group3_ids = patient_counts[patient_counts == 3].index
        group3_df = filtered_df[filtered_df['Número de documento (sin puntos ni comas)'].isin(group3_ids)]
        # Ordenar y tomar el tercer registro de cada paciente
        group3_df = group3_df.sort_values(['Número de documento (sin puntos ni comas)', 'Marca temporal'])
        group3_df = group3_df.groupby('Número de documento (sin puntos ni comas)').nth(2).reset_index()
        fig3 = create_pie_chart(group3_df, "Tercer registro (3 registros)")
        if fig3:
            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.write("No hay pacientes con 3 registros")
    
    # Grupo 4: pacientes con exactamente 4 registros (cuarto registro)
    with col4:
        group4_ids = patient_counts[patient_counts == 4].index
        group4_df = filtered_df[filtered_df['Número de documento (sin puntos ni comas)'].isin(group4_ids)]
        # Ordenar y tomar el cuarto registro de cada paciente
        group4_df = group4_df.sort_values(['Número de documento (sin puntos ni comas)', 'Marca temporal'])
        group4_df = group4_df.groupby('Número de documento (sin puntos ni comas)').nth(3).reset_index()
        fig4 = create_pie_chart(group4_df, "Cuarto registro (4 registros)")
        if fig4:
            st.plotly_chart(fig4, use_container_width=True)
        else:
            st.write("No hay pacientes con 4 registros")
    
    # Mostrar estadísticas actualizadas
    st.sidebar.header("Estadísticas")
    st.sidebar.write(f"Total de registros en rango: {len(filtered_df)}")
    st.sidebar.write(f"Pacientes únicos: {len(patient_counts)}")
    st.sidebar.write(f"Pacientes con 1 registro: {len(group1_df)}")
    st.sidebar.write(f"Pacientes con 2 registros: {len(group2_df)}")
    st.sidebar.write(f"Pacientes con 3 registros: {len(group3_df)}")
    st.sidebar.write(f"Pacientes con 4 registros: {len(group4_df)}")






########################################################################################################################
#
#                                              INDICADORES DE RIESGO CARDIOVASCULA
#
########################################################################################################################


import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de variables y sus tipos
VARIABLES_RIESGO_CV = {
    # Variables categóricas (torta)
    'HTA Diagnosticada': 'categorica',
    'DM tipo 1 diagnosticada': 'categorica',
    'DM tipo 2 diagnosticada': 'categorica',
    'Dislipidemia Diagnosticada': 'categorica',
    'Enfermedad isquémica': 'categorica',
    'Enfermedad renal crónica': 'categorica',
    'Índice de Masa Corporal  (Fórmula IMC=Peso(kg) / Estatura al cuadrado(mt))': 'categorica',
    'Perímetro abdominal': 'categorica',
    'Tabaquismo': 'categorica',
    'Mortalidad': 'categorica',
    'Riesgo Cardiovascular': 'categorica',
    
    # Variables numéricas (barras)
    'Rango HTA': 'numerica',
    'Rango LDL': 'numerica',
    'Colesterol no HDL': 'numerica',
    'TFG': 'numerica',
    'Albumina en orina': 'numerica',
    'Número de episodios de ira en los últimos 6 meses': 'numerica',
    'Índice tobillo brazo': 'numerica',
    'Complicaciones durante el seguimiento': 'numerica',
    'Número de ingresos a urgencias por causa CV en los últimos 3 meses': 'numerica',
    'Número de ingresos a hospitalización por causa CV en los últimos 3 meses': 'numerica'
}

# Orden específico para variables categóricas (si es necesario)
ORDEN_CATEGORIAS = {
    'Rango HTA': ['Normal', 'Pre-HTA', 'HTA Grado 1', 'HTA Grado 2'],
    'Rango LDL': ['Óptimo', 'Casi óptimo', 'Limite alto', 'Alto', 'Muy alto'],
    'Índice de Masa Corporal  (Fórmula IMC=Peso(kg) / Estatura al cuadrado(mt))': ['Bajo peso', 'Normal', 'Sobrepeso', 'Obesidad I', 'Obesidad II']
}

def generar_grafico_trimestral(df, columna: str, tipo: str, trimestre: int):
    """
    Genera gráficos trimestrales para variables de riesgo CV
    """
    # Filtrado por pacientes con exactamente 'trimestre' registros
    patient_counts = df['Número de documento (sin puntos ni comas)'].value_counts()
    group_ids = patient_counts[patient_counts == trimestre].index
    group_df = df[df['Número de documento (sin puntos ni comas)'].isin(group_ids)]
    
    # Para trimestres >1, tomamos la medición correspondiente
    if trimestre > 1:
        group_df = group_df.sort_values(['Número de documento (sin puntos ni comas)', 'Marca temporal'])
        group_df = group_df.groupby('Número de documento (sin puntos ni comas)').nth(trimestre-1).reset_index()
    
    # Manejo de datos faltantes
    group_df = group_df.dropna(subset=[columna])
    
    # Generación del gráfico
    if tipo == 'categorica':
        # Procesamiento para variables categóricas
        counts = group_df[columna].value_counts()
        if columna in ORDEN_CATEGORIAS:
            counts = counts.reindex(ORDEN_CATEGORIAS[columna], fill_value=0)
        fig = px.pie(counts, names=counts.index, values=counts.values,
                    title=f"{columna} (T{trimestre})", hole=0.4)
        fig.update_traces(textposition='inside', textinfo='percent+label')
    else:
        # Procesamiento para variables numéricas
        fig = px.histogram(group_df, x=columna, 
                          title=f"{columna} (T{trimestre})",
                          color_discrete_sequence=['#636EFA'])
        fig.update_layout(bargap=0.1)
    
    return fig

def mostrar_panel_riesgo_cv(df):
    """
    Muestra el panel completo de indicadores de riesgo cardiovascular
    """
    st.header("📊 Panel de Indicadores de Riesgo Cardiovascular (Trimestral)")
    
    for variable, tipo in VARIABLES_RIESGO_CV.items():
        with st.expander(f"**{variable}**", expanded=False):
            cols = st.columns(4)
            
            for trimestre in range(1, 5):
                with cols[trimestre-1]:
                    try:
                        fig = generar_grafico_trimestral(df, variable, tipo, trimestre)
                        st.plotly_chart(fig, use_container_width=True)
                    except Exception as e:
                        st.error(f"Error al generar gráfico: {str(e)}")
                        st.warning(f"Datos insuficientes para {variable} (T{trimestre})")

# Función adicional para resumen estadístico
def mostrar_resumen_estadistico(df):
    """Muestra estadísticas clave del dataset"""
    st.sidebar.header("📈 Resumen Estadístico")
    
    total_pacientes = df['Número de documento (sin puntos ni comas)'].nunique()
    total_registros = len(df)
    fecha_min = df['Marca temporal'].min().strftime('%Y-%m-%d')
    fecha_max = df['Marca temporal'].max().strftime('%Y-%m-%d')
    
    st.sidebar.metric("👥 Pacientes Únicos", total_pacientes)
    st.sidebar.metric("📝 Registros Totales", total_registros)
    st.sidebar.write(f"📅 Rango de fechas: {fecha_min} a {fecha_max}")
    
    # Conteo de registros por paciente
    counts = df['Número de documento (sin puntos ni comas)'].value_counts().value_counts()
    for n, cnt in counts.items():
        st.sidebar.metric(f"Pacientes con {n} registro(s)", cnt)





