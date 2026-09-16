# Quantum-Entanglement
My very first programming project! Exploring the basics of quantum computing using Python.
## Quantum Circuit Architecture

This is how the 6-qubit cascading entanglement chain reaction looks structurally. The Hadamard (`H`) gate puts the first qubit into superposition, and the Controlled-NOT (`X`) gates ripple the entanglement down the entire chain:

     ┌───┐                                             ┌─┐                  
q_0: ┤ H ├──■──────────────────────────────────────────┤M├──────────────────
     └───┘┌─┴─┐                                        └╥┘┌─┐               
q_1: ─────┤ X ├──■──────────────────────────────────────╫─┤M├───────────────
          └───┘┌─┴─┐                                    ║ └╥┘┌─┐            
q_2: ──────────┤ X ├──■─────────────────────────────────╫──╫─┤M├────────────
               └───┘┌─┴─┐                               ║  ║ └╥┘┌─┐         
q_3: ───────────────┤ X ├──■────────────────────────────╫──╫──╫─┤M├─────────
                    └───┘┌─┴─┐                          ║  ║  ║ └╥┘┌─┐      
q_4: ────────────────────┤ X ├──■───────────────────────╫──╫──╫──╫─┤M├──────
                         └───┘┌─┴─┐                     ║  ║  ║  ║ └╥┘┌─┐   
q_5: ─────────────────────────┤ X ├─────────────────────╫──╫──╫──╫──╫─┤M├───
                              └───┘                     ║  ║  ║  ║  ║ └╥┘   
c: 6/═══════════════════════════════════════════════════╩══╩══╩══╩══╩══╩════
                                                        0  1  2  3  4  5    
```
