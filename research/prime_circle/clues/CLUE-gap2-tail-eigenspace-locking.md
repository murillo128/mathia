---
id: CLUE-prime-circle-gap2-tail-eigenspace-locking
type: research-clue
status: proposed
origin: visual-researcher
target_line: prime_circle
based_on:
  - research/prime_circle/findings/PC-139-primorial-hessian-bulk-collapse-hides-mesoscopic-macroscopic-defect-modes.md
  - research/prime_circle/findings/PC-140-primitive-shell-hessian-trace-classicalizes-to-artin-nicolas.md
  - research/prime_circle/findings/PC-141-fixed-edge-fourier-window-classicalizes-to-murata-nicolas.md
  - research/visual_exploration/visualizations/primitive-shell-gap2-spectral-locking.md
---

# Does the gap-two matching nearly identify the whole macroscopic primitive-shell eigenspace?

## Observation

PC-139 gives an exact gap-two matching subspace \(V_x\) of dimension
\(E_x=\prod_{3\le p\le x}(p-2)\) and proves that its Rayleigh quotients force at least \(E_x\) order-\(N_x^2\) defect modes. PC-140 shows that the primitive-shell trace itself collapses to classical Artin/Nicolas arithmetic. PC-141 further rules out every fixed-width Fourier edge window and explicitly leaves localized/non-Fourier organization of the PC-139 modes as a surviving spectral frontier.

Direct diagonalization of the primitive-shell internal Laplacian at \(N=30,210,2310\) shows a much stronger finite pattern. In each case exactly \(E_x=3,15,135\) eigenvalues lie above the PC-139 threshold \(\beta_N=(2\sin^2(2\pi/N))^{-1}\), and the top-\(E_x\) spectral subspace captures `0.996344`, `0.996299`, and `0.996450` of \(V_x\) in normalized squared Frobenius overlap. The smallest squared principal cosines are `0.993857`, `0.992008`, and `0.989871`. At \(N=2310\), projector leverage averages `0.498944` on gap-two-paired vertices and `0.001358` on unpaired vertices.

Same-dimension step-4, step-6, and fixed-seed random matching controls have much smaller overlap; at \(N=2310\) they give `0.276429`, `0.249117`, and `0.282286` respectively.

## Research question

For primorial \(N_x\), does the top \(E_x\)-dimensional eigenspace of the primitive-shell operator \(L_{N_x}^{\rm int}\) stay uniformly close to, or asymptotically approach, the exact gap-two matching subspace \(V_x\)? Is there a uniform \(N_x^2\)-scale spectral gap separating those \(E_x\) modes from the rest?

Equivalently, after decomposing
\[
L_{N_x}^{\rm int}=A_x+R_x,
\qquad
A_x=\beta_{N_x}P_{V_x},
\]
can the block structure of \(R_x\) relative to \(V_x\oplus V_x^\perp\) explain the observed near-locking? A positive answer would substantially classicalize the still-open localized/non-Fourier “mode organization” frontier after PC-139/PC-141; a negative answer should identify the first scale or coupling where genuinely nonlocal organization enters.

## Why it may matter

PC-139 deliberately leaves open the placement and organization of its mesoscopic macroscopic tail, while PC-141 shows that fixed Fourier windows cannot carry the missing mechanism. The visualization suggests that the most prominent localized part of that tail may already be almost exhausted by the local shortest-chord CRT matching, not merely bounded below by it. Proving this would narrow the Prime-Circle spectral frontier and prevent later work from treating these leading modes as unexplained global arithmetic structure. Refuting it at larger scales would instead expose where the local matching approximation breaks and provide a concrete nonlocal statistic to study.

## Decisive test

Analyze \(R_x=L_{N_x}^{\rm int}-A_x\) in the decomposition \(V_x\oplus V_x^\perp\). Prove or disprove a spectral-separation estimate strong enough to control the principal angles between \(V_x\) and the top-\(E_x\) eigenspace, for example through bounds on
\(P_{V_x^\perp}R_xP_{V_x}\) and the two diagonal blocks. Determine whether the projector distance tends to zero, remains uniformly small, or eventually grows.

As a computational falsifier before a proof, use sparse eigensolvers at the next primorial \(N=30030\) to test the spectral cliff and subspace overlap without assuming the finite-\(N\) pattern persists.

## Evidence boundary

The near-locking is finite numerical evidence at three conductors, not a theorem, asymptotic law, novelty claim, or RH mechanism. The gap-two min-max lower bound and matching dimension are established by PC-139, but neither PC-139, PC-141, nor this computation proves that these vectors exhaust the macroscopic tail. The comparison controls only show that the observed alignment is not generic among the tested pair subspaces; short-chord dominance remains a live explanation.
