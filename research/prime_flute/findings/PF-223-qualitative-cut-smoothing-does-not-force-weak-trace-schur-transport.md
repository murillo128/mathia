# PF-223 — qualitative cut smoothing does not force weak-trace Schur transport

**Status:** `EXACT-DERIVED + ABSTRACT-COUNTERMODEL + DECISIVE-NEGATIVE/ROUTE-BOUNDARY`. PF-222 proves that the exact reciprocal-prime Schur commutator in the simultaneous smooth-interface construction is compact: every fixed prefix cut has a smoothing/trace-class flux and the reciprocal-prime layer expansion converges in operator norm. That is a genuine narrowing, but it does **not** supply the missing weak-`S_1` rate. The gap cannot be closed from the qualitative ingredients alone. There is an explicit positive block-Jacobi precision model with the exact reciprocal-prime module weight in which every adjacent precision block is finite rank, every prefix resolvent commutator is finite rank, the low projection has rank one on every module, and `[D,\Omega]` is compact, yet

\[
\boxed{P[D,\Omega]H\notin\mathcal S_{1,\infty}.}
\]

Thus even strengthening PF-222's fixed-edge smoothing to fixed-edge **finite rank**, while strengthening PF-210's logarithmic low-rank bound to rank one, does not turn compactness into the endpoint estimate. The countermodel is not a counterexample to the canonical prime flute: it deliberately allows the quantitative constants/effective ranks of successive thin-pant couplings to degenerate without control. Its force is narrower and exact. Any successful smooth-route proof must use a uniform position-dependent estimate from the actual one-dimensional seam/frequency geometry — for example PF-212 high-frequency decay, a weighted cut-flux bound, or an equivalent quantitative restriction — and cannot conclude weak trace class merely from block-Jacobi support, reciprocal-prime variation, fixed-edge smoothing, compactness, and low rank.

## Claim

Let

\[
\mathcal B=\bigoplus_{n\ge1}\mathcal B_n
\]

with every `\mathcal B_n` separable infinite-dimensional, and let `\Pi_n` be the module projections. Take the exact PF reciprocal-prime weight

\[
\omega_n=P_n^{-1},
\qquad
\Omega=\bigoplus_{n\ge1}\omega_n I_{\mathcal B_n},
\qquad
\omega_n\downarrow0.
\tag{1}
\]

There exist:

- a positive self-adjoint block-Jacobi operator `K\ge0` on `\mathcal B`;
- its bounded positive contraction `D=(I+K)^{-1}`;
- a module-diagonal orthogonal projection `P` with
  \[
  \operatorname{rank}(P\Pi_n)=1\qquad\text{for every }n;
  \tag{2}
  \]
- `H=I-P`;

such that all of the following hold.

1. Every adjacent block `\Pi_{n+1}K\Pi_n` is finite rank. In particular it lies in `\mathcal S_p` for every `p>0`, with no uniform bound in `n` asserted.
2. For every prefix projection
   \[
   E_m=\sum_{n\le m}\Pi_n,
   \tag{3}
   \]
   the bounded commutator `[D,E_m]` is finite rank, hence belongs to every `\mathcal S_p`.
3. The reciprocal-prime commutator is compact:
   \[
   [D,\Omega]\in\mathcal K(\mathcal B).
   \tag{4}
   \]
4. Nevertheless the exact low/high transport is compact but not weak trace class:
   \[
   \boxed{
   P[D,\Omega]H\in\mathcal K(\mathcal B)
   \setminus\mathcal S_{1,\infty}.
   }
   \tag{5}
   \]

The same `\Omega` still has PF-222's norm-convergent prefix decomposition

\[
\Omega=\sum_{m\ge1}(\omega_m-\omega_{m+1})E_m,
\tag{6}
\]

so (5) is compatible with all of the *qualitative* compactness structure isolated there.

## 1. Build disjoint finite transport packets

Construct disjoint finite module intervals recursively. Once the previous interval ends, choose the next source index `s_j` beyond it. Set

\[
r_j:=\left\lceil\frac{12j}{\omega_{s_j}}\right\rceil.
\tag{7}
\]

Because `\omega_n\to0`, choose `M_j>s_j` so far out that

\[
\omega_m\le\frac12\omega_{s_j}
\qquad(m\ge M_j).
\tag{8}
\]

Use the `r_j` distinct destination indices

\[
t_{j,k}=M_j+k,
\qquad 1\le k\le r_j,
\tag{9}
\]

and let the `j`th packet occupy the finite interval from `s_j` through `t_{j,r_j}`. The next `s_{j+1}` is chosen after that endpoint, so packets are mutually disjoint.

For every channel `(j,k)` choose orthonormal vectors

\[
e_{j,k,n}\in\mathcal B_n,
\qquad s_j\le n\le t_{j,k},
\tag{10}
\]

with different channels orthogonal even when they pass through the same module. Each module meets only finitely many channels because each packet contains finitely many of them.

On the finite channel space

\[
\mathcal C_{j,k}
=\operatorname{span}\{e_{j,k,n}:s_j\le n\le t_{j,k}\},
\tag{11}
\]

choose a unit vector `v_{j,k}` whose source and destination coordinates carry almost all the mass. If `L=t_{j,k}-s_j-1` is the number of interior sites, take unnormalized endpoint coordinates equal to `1` and every interior coordinate equal to

\[
\eta=(10\sqrt L)^{-1}.
\tag{12}
\]

Then the squared norm before normalization is `2.01`, so after normalization

\[
(v_{j,k})_{s_j}(v_{j,k})_{t_{j,k}}
=\frac1{2.01}>0.49.
\tag{13}
\]

(Choosing the intervals with at least one interior site makes (12) literal; any fixed harmless modification covers the finite head.)

## 2. A positive nearest-neighbor precision can transmit each channel with order-one amplitude

On `\mathcal C_{j,k}` define the positive quadratic form

\[
q_{j,k}[x]
=
\sum_{n=s_j}^{t_{j,k}-1}
\left|
\frac{x_n}{(v_{j,k})_n}
-
\frac{x_{n+1}}{(v_{j,k})_{n+1}}
\right|^2.
\tag{14}
\]

Its matrix `Q_{j,k}` is positive and tridiagonal, and

\[
\ker Q_{j,k}=\mathbb C v_{j,k}.
\tag{15}
\]

Let `\gamma_{j,k}>0` be its smallest positive eigenvalue. Choose a finite scalar `\lambda_{j,k}` so large that

\[
(1+\lambda_{j,k}\gamma_{j,k})^{-1}\le\frac1{12},
\tag{16}
\]

and put

\[
K_{j,k}=\lambda_{j,k}Q_{j,k},
\qquad
D_{j,k}=(I+K_{j,k})^{-1}.
\tag{17}
\]

The spectral decomposition at the one-dimensional kernel gives

\[
D_{j,k}=|v_{j,k}\rangle\langle v_{j,k}|+R_{j,k},
\qquad
\|R_{j,k}\|\le\frac1{12}.
\tag{18}
\]

Hence the source-to-destination matrix element obeys

\[
\begin{aligned}
\langle e_{j,k,t_{j,k}},D_{j,k}e_{j,k,s_j}\rangle
&\ge
(v_{j,k})_{t_{j,k}}(v_{j,k})_{s_j}-\frac1{12}\\
&>\frac13.
\end{aligned}
\tag{19}
\]

Now define `K` as the orthogonal direct sum of all `K_{j,k}` on the mutually orthogonal channel spaces and as zero on their orthogonal complement. This is a positive self-adjoint operator on its natural direct-sum domain. Its norm may diverge from packet to packet; that is intentional. Relative to the module decomposition it is block Jacobi, because every form (14) contains only diagonal and nearest-neighbor terms.

For a fixed module edge `n\leftrightarrow n+1`, only finitely many channels cross it. Therefore

\[
\Pi_{n+1}K\Pi_n
\]

is finite rank for every fixed `n`, even though its rank and norm need not be uniform along the tail. With

\[
D=(I+K)^{-1},
\tag{20}
\]

we have `0\le D\le I` exactly as in the normalized Schur setup.

## 3. Rank-one low sectors still allow arbitrarily large transport multiplicity across a packet

Choose the low projection `P` module by module. At every destination module `t_{j,k}`, let the unique low vector be the corresponding endpoint `e_{j,k,t_{j,k}}`. At every other module choose one filler vector orthogonal to all active channel vectors. Thus (2) holds exactly. All source and intermediate channel vectors lie in `H=I-P`; at a module that is the destination of a different channel, orthogonality of the channel labels still makes the current channel vector high.

For a source vector `e_{j,k,s_j}`, the projection `P` kills every component of `D e_{j,k,s_j}` except its own destination endpoint. Therefore

\[
P[D,\Omega]H e_{j,k,s_j}
=
(\omega_{s_j}-\omega_{t_{j,k}})
\langle e_{j,k,t_{j,k}},D e_{j,k,s_j}\rangle
e_{j,k,t_{j,k}}.
\tag{21}
\]

By (8) and (19), every one of these `r_j` mutually orthogonal source/destination pairs has singular amplitude at least

\[
\boxed{
\frac{\omega_{s_j}}6.
}
\tag{22}
\]

Let

\[
\sigma_j=\frac{\omega_{s_j}}{12}.
\tag{23}
\]

The singular-value counting function of

\[
T:=P[D,\Omega]H
\tag{24}
\]

therefore satisfies

\[
N_T(\sigma_j)\ge r_j.
\tag{25}
\]

Using (7),

\[
\boxed{
\sigma_jN_T(\sigma_j)
\ge
\frac{\omega_{s_j}}{12}
\frac{12j}{\omega_{s_j}}
\ge j.
}
\tag{26}
\]

The weak trace ideal is characterized by bounded `\sup_{\sigma>0}\sigma N_T(\sigma)` (equivalently `s_m(T)=O(m^{-1})`). Equation (26) proves

\[
\boxed{T\notin\mathcal S_{1,\infty}.}
\tag{27}
\]

No asymptotic theorem about prime gaps or prime density enters this obstruction. Only the exact monotone reciprocal-prime sequence `\omega_n=P_n^{-1}\downarrow0` is used.

## 4. The same model still satisfies PF-222's qualitative compactness gates

The failure (27) is not a disguised noncompactness example of the kind already used in PF-213. On the `j`th finite packet, all module weights are at most `\omega_{s_j}`. Since `\|D\|\le1`,

\[
\|[D,\Omega]\|_{\text{packet }j}
\le2\omega_{s_j}
\longrightarrow0.
\tag{28}
\]

Each packet is finite-dimensional, packets are orthogonal, and their starting indices tend to infinity. Hence the direct sum is compact:

\[
[D,\Omega]\in\mathcal K,
\qquad
T=P[D,\Omega]H\in\mathcal K.
\tag{29}
\]

Likewise, fix one prefix cut `E_m`. Because the packet intervals are disjoint, the cut crosses at most one packet. Only finitely many finite-dimensional channels in that packet meet both sides of the cut. Thus

\[
\boxed{[D,E_m]\text{ is finite rank for every fixed }m.}
\tag{30}
\]

Consequently the exact layer identity (6) expresses `[D,\Omega]` as the same kind of norm limit of finite-ideal cut fluxes used in PF-222, yet the limit can have singular values slower than the weak-`S_1` threshold.

The construction also sharpens the earlier PF-213 warning in a second direction. PF-213 showed that positivity alone can funnel rank-one low modes into a fixed nondecaying module and destroy compactness. Here no fixed nondecaying target survives, every prefix flux is finite rank, and the full commutator is compact. What breaks the endpoint is instead **uncontrolled effective transport multiplicity at scales whose operator norm tends to zero**. That is exactly the distinction the post-PF-222 gate needs to respect.

## 5. Prior art and novelty audit

No novelty is claimed for the operator-ideal facts used in the proof. The singular-value and symmetrically normed ideal framework is classical; see Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., Mathematical Surveys and Monographs 120, AMS (2005). Direct-sum membership in Lorentz--Schatten classes is also an explicit subject of P. Ipek Al, *Lorentz-Schatten classes of direct sum of operators*, Hacettepe Journal of Mathematics and Statistics 49 (2020), 835--842, DOI `10.15672/hujms.522814`. The criterion exploited in (26) is simply the defining weak-`\ell^1` singular-value threshold.

A targeted literature search did not identify a theorem whose hypotheses reduce the present block-Jacobi/fixed-edge qualitative data to weak trace class without a quantitative uniform ideal estimate. This is expected: compactness and membership of every individual block/cut in all Schatten classes place no uniform restriction on how the effective ranks or constants can grow before the block norms tend to zero.

The durable project-specific content is therefore **not** a new general theorem about Lorentz ideals. It is the exact falsification of a tempting PF-222 inference: even with the same reciprocal-prime layer weight, positive block-Jacobi precision, rank-one low sectors, fixed-edge finite rank, and finite-rank prefix fluxes, weak trace class need not follow. The actual prime flute must win through geometric quantitative structure absent from this abstract model.

## 6. Falsification and boundary checks

1. The countermodel does **not** claim that the canonical PF normalized pant blocks have the pathological effective ranks or constants used above. Each abstract packet is finite but can be arbitrarily large; the actual one-dimensional seam kernel has additional frequency structure.
2. The construction deliberately permits the norms of the local precision forms to grow without a uniform tail bound, consistent with the qualitative situation left open after PF-215. It would not falsify a theorem that assumes a quantitative PF-specific bound on those norms or singular values.
3. Rank one in (2) is stronger than PF-210's `O(1+\log P_n)` low-rank estimate. The failure is therefore not caused by replacing the low sector by a cell-scale rank.
4. Every adjacent `K` block and every prefix commutator `[D,E_m]` is finite rank, stronger than the fixed-edge smoothing statement in PF-222. The failure is not caused by a noncompact cut flux.
5. The long channels exploit high source directions and increasingly large finite transport packets. PF-212's physical high-frequency Poisson singular-value decay is intentionally absent. Therefore (27) says that **that sort of quantitative frequency information is necessary to the proof architecture**, not that it is insufficient in the actual flute.
6. The model proves only failure of the abstract implication `qualitative PF-222 structure => weak trace`. It does not prove that the real `P[D,\Omega]H` fails `\mathcal S_{1,\infty}`.
7. Nothing here changes PF-204's unsmoothed native route, PF-183's true-short-collar splice, wave-operator questions, determinants/resonances, prime/clone separation, or any RH consequence.

## Consequences for the research line

PF-222 settles the compactness question and leaves singular-value counting. PF-223 now rules out one entire class of shortcuts for that counting problem. It is not enough to combine reciprocal-prime finite variation with the statements “every pant crossing is smoothing,” “every prefix commutator is trace class,” and “the low sector has small module rank.” Those are qualitative statements and admit the countermodel above.

The next smooth-route theorem must bind **quantity to position**. Useful targets include a `j`-dependent ideal bound for `P[D,E_j]H` that is summable after multiplication by `\delta_j`, a direct counting estimate for the norm-convergent cut-flux series, or a factorization that inserts PF-212's actual high-frequency singular-value envelope before the large transport multiplicity can accumulate. A negative continuation must be correspondingly stronger than PF-223: it would have to realize bad weak-`S_1` counting within the genuine thin-pant DtN/frequency geometry rather than in an abstract block-Jacobi model.