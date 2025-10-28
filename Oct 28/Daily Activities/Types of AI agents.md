# Single-Agent vs Multi-Agent Systems

## 1. What is an Agent?

An **agent** is an autonomous entity that perceives its environment through sensors and acts upon it through actuators to achieve specific goals.

**Formal Definition:**
Agent = Perception + Decision Making + Action

###  Architecture Diagram

![Multi-Agent Architecture](https://images.prismic.io/encord/Z1nNgpbqstJ98V8Q_image4.png?auto=format,compress)
---

**Single Agent Explanation:**
- The agent perceives the **environment** through sensors.
- Based on the **percepts**, it makes a **decision** using an internal model or policy.
- It then performs an **action** that affects the environment.


---
**Multi Agent Explanation:**
- Each agent perceives the environment and other agents.
- Agents communicate through a **shared communication medium** or **direct messages**.
- The overall system behavior emerges from their interactions.

---

## 2. Single-Agent System

###  Definition
A **Single-Agent System** involves **only one intelligent agent** interacting with its environment to achieve a specific goal.  
There are **no other intelligent agents** competing or cooperating in this system.

---

###  Examples
- A robot vacuum cleaner navigating a room.
- A chess-playing AI vs a human (non-AI) opponent.
- A route-finding system (Google Maps).
- A thermostat maintaining room temperature.

---

###  Characteristics

| Feature | Description |
|----------|-------------|
| **Number of agents** | Only one |
| **Goal** | Focused on maximizing its own performance |
| **Environment** | Interacts only with environment |
| **Complexity** | Relatively low |
| **Coordination** | Not required |
| **Communication** | None or minimal |

---

###  Example Scenario
A **self-driving car** on an empty road:
- Senses lanes, obstacles, and signs.  
- Decides speed and steering.  
- Does not coordinate with other vehicles.

---

## 3. Multi-Agent System (MAS)

###  Definition
A **Multi-Agent System (MAS)** is composed of **two or more intelligent agents** that **interact** — either **cooperatively**, **competitively**, or both — to achieve individual or collective goals.

> MAS emphasizes **distributed intelligence**, where agents have partial control and knowledge, and global intelligence emerges through interaction.


---

###  Examples
- Swarm drones performing search and rescue.  
- Autonomous delivery robots in a warehouse.  
- Trading bots competing in financial markets.  
- Smart grids managing distributed power sources.

---

###  Characteristics

| Feature | Description |
|----------|-------------|
| **Number of agents** | Two or more |
| **Goal** | May be shared (cooperative) or conflicting (competitive) |
| **Environment** | Shared among agents |
| **Complexity** | Higher, due to interaction |
| **Coordination** | Often necessary |
| **Communication** | Required, explicit or implicit |

---

## 4. Types of Multi-Agent Interactions

| Type | Description | Example |
|------|--------------|---------|
| **Cooperative** | Agents work together for a shared goal. | Swarm robots cleaning an area. |
| **Competitive** | Agents have conflicting goals. | Trading bots in stock markets. |
| **Mixed** | Agents cooperate in some aspects and compete in others. | Autonomous cars managing intersections. |

---

## 5. Key Differences

| Aspect | **Single-Agent System** | **Multi-Agent System** |
|--------|--------------------------|------------------------|
| **Number of Agents** | One | Multiple |
| **Interaction** | With environment only | With environment + other agents |
| **Coordination** | Not needed | Essential |
| **Communication** | None | Explicit/Implicit |
| **Decision Making** | Centralized | Distributed |
| **Complexity** | Lower | Higher |
| **Goal Structure** | Single goal | Shared or conflicting goals |
| **Example** | Vacuum robot | Drone swarm or smart traffic system |

---

## 6. Advantages & Challenges

###  Single-Agent Systems
**Advantages**
- Easier to design and train  
- No need for negotiation or coordination  
- Clear performance metric  

**Challenges**
- Limited scalability  
- Inefficient for distributed tasks  

---

###  Multi-Agent Systems
**Advantages**
- Scalable and flexible  
- Robust (failure of one agent doesn’t break the system)  
- Parallel operation  
- Emergent intelligent behavior  

**Challenges**
- Communication overhead  
- Conflict resolution  
- Unpredictable emergent behaviors  

---

## 7. Real-World Applications

| Domain | Example | Type |
|--------|----------|------|
| **Robotics** | Robot vacuum cleaner | Single-Agent |
| **Autonomous Vehicles** | Multiple cars negotiating traffic | Multi-Agent |
| **E-commerce** | Price optimization bot | Single-Agent |
| **Financial Markets** | Competing trading bots | Multi-Agent |
| **Smart Grids** | Energy balancing among producers/consumers | Multi-Agent |
| **Games** | Chess-playing AI | Single-Agent |
| **Online Games** | Team-based AI bots | Multi-Agent |

---

## 8. Summary

| Criteria | **Single-Agent** | **Multi-Agent** |
|-----------|------------------|----------------|
| **Agents** | One | Many |
| **Goal Alignment** | Single | Shared/Conflicting |
| **Decision Making** | Centralized | Distributed |
| **Interaction** | Only with environment | With environment + agents |
| **Complexity** | Low | High |
| **Example** | Pathfinding robot | Smart traffic network |

---

## 9. In Simple Terms

-  **Single-Agent**: “I act alone to achieve my goal.”  
-  **Multi-Agent**: “We act together (or compete) — my success depends on others too.”

