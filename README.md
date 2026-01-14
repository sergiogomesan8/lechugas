# Proyecto Lechugas 🥬

![Lechugas](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmk4c3U5ODVwMzNlZ2pjaTRlNWZpZ2l0bXcxZXFmMTk4bm92aXplMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dd2wy16j3pwOpaE4XG/giphy.gif)

## Descripción

Este proyecto es una **recreación divertida y técnica** del famoso “problema de las lechugas” de Mercadona: cómo contar productos de manera eficiente y precisa.  

Aquí llevamos la gestión de lechugas al siguiente nivel usando **Python**, **arquitectura hexagonal**, **Domain-Driven Design (DDD)** y un enfoque **event-driven** con **RabbitMQ**.  

El proyecto está compuesto por **dos servicios principales**:  

- **Order Service**: maneja la venta de productos.  
- **Stock Service**: lleva la cuenta de las lechugas y actualiza el inventario.  

Se pueden experimentar diferentes estrategias de manejo de stock y persistencia:  
- Actualizaciones **pesimistas** vs **optimistas**.  
- Versionado de stock y control de concurrencia.  
- Persistencia en base de datos para garantizar consistencia y eficiencia.  

---

## Objetivos

- Explorar conceptos de **DDD** y **arquitectura hexagonal** en un ejemplo divertido y realista.  
- Practicar **event-driven architecture** con RabbitMQ.  
- Implementar patrones de gestión de stock y estrategias de persistencia.  
- Aprender sobre sincronización y consistencia en sistemas distribuidos… todo con lechugas 😄.  

---

## Tecnologías

- **Python**  
- **RabbitMQ**  
- Base de datos relacional o NoSQL (según la estrategia probada)  
- Arquitectura hexagonal  
- Domain-Driven Design (DDD)  

---

## Cómo usarlo

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/proyecto-lechugas.git
cd proyecto-lechugas
