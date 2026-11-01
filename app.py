\begin{figure}[h!]
    \centering
    \begin{circuitikz}[scale=1.2, transform shape]
        % Cable izquierdo (fuente de voltaje en cortocircuito)
        \draw (0,0) -- (0,4);
        
        % Rama superior (R1) e inferior (R6)
        \draw (0,4) to[R, l=$R_1$] (3,4);
        \draw (0,0) to[R, l_=$R_6$] (3,0);
        
        % Rama vertical central (R2 y cable)
        \draw (3,4) to[R, l=$R_2$] (3,2);
        \draw (3,2) -- (3,0);
        
        % Extensiones de los cables superior e inferior
        \draw (3,4) -- (6,4);
        \draw (3,0) -- (6,0);
        
        % Rama horizontal central (R4)
        \draw (3,2) to[R, l=$R_4$] (6,2);
        
        % Rama vertical derecha (R3 y R5)
        \draw (6,4) to[R, l=$R_3$] (6,2);
        \draw (6,2) to[R, l=$R_5$] (6,0);
        
        % Terminales a y b
        \draw (6,2) -- (7.5,2) node[right] {$a$};
        \draw (6,0) -- (7.5,0) node[right] {$b$};
    \end{circuitikz}
    \caption{Circuito equivalente para el cálculo de la Resistencia de Thévenin.}
    \label{fig:circuito_rth}
\end{figure}
