# Primitive-shell gap-2 spectral locking

![Primitive-shell gap-2 spectral locking](./primitive-shell-gap2-spectral-locking.png)

## Question

PC-139 proves that gap-two pairs in the primitive shell give an exact matching of dimension
\(E_x=\prod_{3\le p\le x}(p-2)\) and therefore force at least \(E_x\) macroscopic defect modes. PC-140 then shows that the scalar trace of the same primitive-shell operator classicalizes to Artin/Nicolas data. Is the unresolved **organization** of the macroscopic tail also largely determined by the gap-two matching, or do the other within-shell edges reorganize those modes substantially?

## Construction

For the primorial conductors \(N=30,210,2310\), take the primitive shell \(U(N)\) and its internal inverse-square chord Laplacian
\[
(L_N^{\rm int})_{ab}=
\begin{cases}
-\bigl(4\sin^2(\pi(a-b)/N)\bigr)^{-1},&a\ne b,\\
\sum_{c\ne a}\bigl(4\sin^2(\pi(a-c)/N)\bigr)^{-1},&a=b,
\end{cases}
\qquad a,b\in U(N).
\]

Let \(\mathcal E_N=\{\{a,a+2\}:a,a+2\in U(N)\}\). By PC-139 these edges form an exact matching. With
\(q_e=(e_a-e_{a+2})/\sqrt2\), let \(V_N=\operatorname{span}\{q_e:e\in\mathcal E_N\}\), \(\dim V_N=E\), and let \(W_N\) be the span of the top \(E\) eigenvectors of \(L_N^{\rm int}\).

The plot compares the normalized spectrum, the principal angles between \(V_N\) and \(W_N\), the diagonal leverage of the projector onto \(W_N\) around the \(N=2310\) residue circle, and same-dimension controls. The random control uses 128 uniformly shuffled vertex matchings with fixed seed `20260903`; step-4 and step-6 controls use deterministic disjoint pairings inside \(U(N)\).

## Visual observation

The numerical spectrum has a sharp cliff at exactly the gap-two matching dimension in all three samples. The number of eigenvalues at least the PC-139 threshold
\(\beta_N=(2\sin^2(2\pi/N))^{-1}\) is exactly \(E=3,15,135\) for \(N=30,210,2310\), while the next normalized eigenvalue drops from approximately \(0.0138\) to \(0.00626\) at \(N=2310\).

More strikingly, \(V_N\) and the top-\(E\) spectral subspace are almost the same finite-dimensional subspace. Their normalized Frobenius capture
\[
E^{-1}\|Q_N^\top U_{N,\mathrm{top}}\|_F^2
\]
is `0.996344`, `0.996299`, and `0.996450`, respectively. Even the smallest squared principal cosine is `0.993857`, `0.992008`, and `0.989871`. At \(N=2310\), the mean top-\(E\) projector leverage is `0.498944` on vertices belonging to a gap-two pair and only `0.001358` on unpaired primitive residues. The circular panel makes this localization visible directly.

## Controls / robustness

The alignment is not reproduced by arbitrary same-dimension pair subspaces. For \(N=2310\), the captured fractions are `0.276429` for the deterministic step-4 matching, `0.249117` for step-6, and `0.282286` for the mean of the 128 random matchings, versus `0.996450` for gap two. The corresponding random-control means at \(N=30,210\) are `0.417239` and `0.319607`, again far below the gap-two values.

The observation is basis-invariant because it uses principal angles and spectral projectors rather than individual eigenvectors, which can rotate inside degenerate eigenspaces. It is still only a bounded computation at three primorials. Short-chord dominance is an obvious alternative explanation, so the picture must not be interpreted as an RH-specific spectral phenomenon.

## Research consequence

The finite data suggest a sharper continuation of PC-139: the guaranteed gap-two matching may not merely provide a min-max lower bound; it may nearly *identify the entire macroscopic primitive-shell tail* as a spectral subspace. That would further narrow the surviving Prime-Circle mechanism, because the leading non-universal modes would be controlled by a very local CRT/short-chord structure rather than by an unknown global eigenvector organization.

This is handed to Prime Circle as [[research/prime_circle/clues/CLUE-gap2-tail-eigenspace-locking.md]]. The decisive question is whether the observed projector alignment and spectral separation admit a uniform or asymptotic proof after writing \(L_N^{\rm int}\) as the exact gap-two matching Laplacian plus the remaining positive operator.
