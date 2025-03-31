# 🔍 Log Analysis Tool

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Una herramienta para monitorear y analizar logs en tiempo real o en modo repetitivo. Detecta patrones personalizados usando expresiones regulares y genera alertas.

## 🚀 Características Principales

- **Monitoreo en tiempo real** (Modo 0)
- **Alertas personalizables** con Regex
- **Configuración simple** mediante archivo `config.ini`
- **Modo repetitivo** para análisis programados
- **Retardo ajustable** entre detecciones

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/infernoidpl4y/Log_Analyzer.git
cd Log_Analyzer
```

#⚙ Configuración 

Crea un archivo config.ini con esta estructura:
```
# config.ini
File /ruta/al/archivo.log  # Ruta del log a analizar
Mode 3                     # 0 = infinito, 1+ = repeticiones
Sleep 1                    # Segundos de espera tras cada alerta

# Sintaxis: Alert <NOMBRE_ALERTA> "<patrón_regex>"
Alert Error_404 "404"
Alert SQL_Injection "('|\")(;|--).*((SELECT|INSERT|DELETE|UPDATE)|(UNION.*SELECT))"
```
# Opciones de Configuración
```
Opción	Descripción
File	Ruta absoluta o relativa al archivo de log
Mode	0 = Ejecución continua, 1+ = Número de análisis consecutivos
Sleep	Tiempo de pausa (segundos) tras cada alerta detectada
Alert	Define alertas con formato: Nombre "patrón_regex" (entre comillas)
```
🖥 Uso

Ejecuta el analizador:
```
python3 log_analyzer.py
```
Ejemplo de salida:
```
[+] Alerta Error_404 en línea 42:
    192.168.1.1 - GET /pagina.html 404 Not Found
[+] Alerta SQL_Injection en línea 87:
    10.0.0.5 - POST /login.php?query='; SELECT * FROM users;--
Total detectado: 2 alertas
```
🔧 Escenarios de Uso

1. Monitoreo Continuo (Modo 0)
```
File /var/log/nginx/access.log
Mode 0
Sleep 2
Alert Error_500 "5\d{2}"
```
2. Análisis Programado (Modo 5)

Modo >= 1 ; Cantidad de veces que se repite el análisis
```
File /logs/errores_aplicacion.log
Mode 5
Sleep 0
Alert Timeout "Timeout expired"
```
