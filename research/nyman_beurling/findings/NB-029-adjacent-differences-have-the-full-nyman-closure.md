# NB-029 — adjacent differences have the full Nyman closure

**Status:** `EXACT-DERIVED + TELESCOPING-CLOSURE-EQUIVALENCE + FINITE-SECTION-TRANSFER + NEGATIVE/NUISANCE-QUOTIENT-BOUNDARY`. `NB-025`--`NB-026` identify adjacent-generator cancellations as a large source-independent supply of low-Rayleigh, asymptotically target-poor directions, while `NB-027`--`NB-028` test whether the target-selected coefficient vector can be separated from those directions. There is a stronger topological obstruction to treating the complete adjacent family as disposable nuisance: **the adjacent differences themselves generate exactly the same closed Hilbert subspace as the full canonical discrete Nyman family.**

Let

\[
V_N:=\operatorname{span}(g_2,\ldots,g_N),
\qquad
V_\infty:=\overline{\bigcup_{N\ge2}V_N},
\tag{1}
\]

and define

\[
h_n:=g_n-g_{n+1},\qquad n\ge2,
\tag{2}
\]

\[
W_M:=\operatorname{span}(h_2,\ldots,h_{M-1}),
\qquad
W_\infty:=\overline{\bigcup_{M\ge3}W_M}.
\tag{3}
\]

Then

\[
\boxed{W_\infty=V_\infty.}
\tag{4}
\]

Indeed, every `h_n` lies in `V_(n+1)`, so `W_infinity subseteq V_infinity`. Conversely, for every fixed `n` and every `M>n`,

\[
\sum_{k=n}^{M-1}h_k=g_n-g_M.
\tag{5}
\]

The canonical generator bound used in `NB-027`--`NB-028`,

\[
\|g_M\|^2\le\frac2M,
\tag{6}
\]

shows that the right side of (5) converges in Hilbert norm to `g_n`. Thus every canonical generator belongs to `W_infinity`, proving (4).

Consequently, if

\[
d_N:=\operatorname{dist}(e,V_N),
\qquad
\delta_M:=\operatorname{dist}(e,W_M),
\tag{7}
\]

then

\[
\boxed{
\delta_M\downarrow
\operatorname{dist}(e,W_\infty)
=
\operatorname{dist}(e,V_\infty)
=
\lim_{N\to\infty}d_N.
}
\tag{8}
\]

Combined with the discrete Báez-Duarte form of the Nyman--Beurling criterion, this means that RH is equivalently the closure of the target by finite linear combinations of the successive differences `g_n-g_(n+1)`. That reformulation is **not** presented as a new route to RH or as novelty by itself. Its role here is adversarial: the entire family that supplies the most obvious universal low-Rayleigh nuisance atoms cannot be quotiented away asymptotically without quotienting away the whole Nyman approximation space.

There is also a quantitative finite-section transfer. For any

\[
v_N=\sum_{n=2}^{N}a_ng_n\in V_N,
\qquad
A:=\sum_{n=2}^{N}a_n,
\tag{9}
\]

and any `M>N`, set

\[
C_k:=\sum_{n=2}^{\min(k,N)}a_n,
\qquad 2\le k<M.
\tag{10}
\]

Termwise telescoping gives the exact identity

\[
\boxed{
\sum_{k=2}^{M-1}C_kh_k=v_N-A g_M.
}
\tag{11}
\]

For the canonical best approximant `v_N=P_(V_N)e`, write `A_N=sum_(n=2)^N a_(N,n)`. Then (11) gives

\[
\boxed{
\delta_M\le d_N+|A_N|\,\|g_M\|.
}
\tag{12}
\]

`NB-028` identifies the endpoint coefficient exactly as

\[
A_N=1-M(N)+E_N(N),
\qquad
|E_N(N)|\le4Nd_N,
\tag{13}
\]

where `M(N)=sum_(n<=N)mu(n)`. Hence

\[
\boxed{
\delta_M
\le d_N+
\sqrt{\frac2M}
\bigl(|1-M(N)|+4Nd_N\bigr).
}
\tag{14}
\]

No cancellation theorem is needed to obtain a uniform transfer after a mild section enlargement. Since `|M(N)|<=N` and `d_N<=\|e\|=1`,

\[
\boxed{
\delta_M
\le d_N+(1+5N)\sqrt{\frac2M}.
}
\tag{15}
\]

Thus for any positive sequence `L_N->infinity`, with

\[
M_N:=\left\lceil N^2L_N^2\right\rceil,
\tag{16}
\]

one has

\[
\boxed{
\delta_{M_N}\le d_N+O(L_N^{-1}).
}
\tag{17}
\]

For example,

\[
\boxed{
\delta_{\lceil N^2(\log N)^2\rceil}
\le d_N+O\!\left(\frac1{\log N}\right).
}
\tag{18}
\]

At the exact quadratic enlargement, the classical PNT consequence `M(N)=o(N)` already anchored for `NB-028` gives a sharper conditional-on-closure comparison: along any subsequence with `d_N->0`,

\[
\boxed{\delta_{N^2}\longrightarrow0.}
\tag{19}
\]

The point of (12)--(19) is not that the adjacent-difference family improves the known approximation rate. It is that the closure equality (4) is quantitatively visible at finite scale: a canonical Nyman approximant can be transported into a finite adjacent-difference section, and the entire transport loss is an endpoint mode `A_N g_M`. This is the Hilbert-space counterpart of the one-dimensional coefficient quotient exposed by `NB-028`.

## 1. The closure identity is a general telescoping lemma

The mechanism behind (4) is elementary. If `(x_n)` is any sequence in a Hilbert space with `x_n->0`, then

\[
\overline{\operatorname{span}\{x_n:n\ge n_0\}}
=
\overline{\operatorname{span}\{x_n-x_{n+1}:n\ge n_0\}}.
\tag{20}
\]

One inclusion is immediate because every difference belongs to the span of two consecutive `x_n`. For the other, fix `n` and telescope:

\[
x_n-x_M=\sum_{k=n}^{M-1}(x_k-x_{k+1})
\longrightarrow x_n.
\tag{21}
\]

The Nyman specialization uses only the vanishing norm (6). Therefore the topological statement does not depend on Möbius locking, RH, the target, Gram eigenvalues, or the best-approximation normal equations.

This universality is exactly why the result is a **negative control**, not an arithmetic mechanism. The arithmetic content enters only when one asks how efficiently a particular target-selected finite approximant transfers between the two finite dictionaries; there `A_N` is identified by the shell Möbius relation of `NB-028`.

## 2. Exact finite transfer and the endpoint quotient

Apply (5) separately to every generator in (9):

\[
g_n=\sum_{k=n}^{M-1}h_k+g_M.
\tag{22}
\]

Multiplying by `a_n`, summing over `2<=n<=N`, and reversing the finite triangular sum gives

\[
\begin{aligned}
v_N
&=\sum_{n=2}^{N}a_n\sum_{k=n}^{M-1}h_k
 +\left(\sum_{n=2}^{N}a_n\right)g_M\\
&=\sum_{k=2}^{M-1}
\left(\sum_{n=2}^{\min(k,N)}a_n\right)h_k
+A g_M,
\end{aligned}
\tag{23}
\]

which proves (11).

Therefore

\[
V_N\subseteq W_M+\operatorname{span}\{g_M\}
\qquad(M>N).
\tag{24}
\]

The quotient direction is not abstract: it is exactly the terminal generator. Its norm tends to zero, so this finite codimension-one defect disappears in the ambient Hilbert topology as `M` grows.

For the best approximant, define

\[
w_{N,M}:=
\sum_{k=2}^{M-1}C_kh_k
=P_{V_N}e-A_Ng_M\in W_M.
\tag{25}
\]

Then

\[
e-w_{N,M}=r_N+A_Ng_M,
\tag{26}
\]

and the triangle inequality proves (12). Substituting (6) and the exact `NB-028` endpoint formula proves (14), while the trivial estimates `|M(N)|<=N` and `d_N<=1` prove (15)--(18).

Equation (19) follows because PNT gives `M(N)=o(N)` and `d_N->0` gives `Nd_N=o(N)`. Thus (13) yields `A_N=o(N)` along a closure subsequence, while `||g_(N^2)||=O(1/N)`.

No converse finite bound of comparable scale is asserted. Although `W_M subseteq V_M` gives

\[
d_M\le\delta_M,
\tag{27}
\]

nothing here proves `delta_M-d_M` small at the **same** section index `M`, because the relevant endpoint coefficient of a finite best approximant may be large. Equality of the infinite closures must not be silently upgraded to uniform finite-section conditioning.

## 3. Why this changes the adjacent-mode interpretation

`NB-025` proves that each large-index normalized adjacent difference `h_n/||h_n||` has target angle tending to zero and that its associated two-coordinate normalized-Gram vector has Rayleigh quotient `O(log n/n)`. `NB-026` packs disjoint such edges into a macroscopic target-poor low-Rayleigh sector. These are valid finite controls: a small eigenvalue or even many small eigenvalues need not be source-selected.

But target-poor **atoms** need not generate a target-poor **closed span**. Equation (5) gives the explicit failure of that inference. To recover `g_n`, one sums a long consecutive block of adjacent differences; the small target couplings and small Hilbert norms of individual high-index atoms can accumulate coherently while the terminal error `g_M` vanishes. The complete adjacent family therefore retains all target approximation capacity despite the asymptotic weakness of each local edge.

This also explains the transition from `NB-027` to `NB-028`. Keeping one disjoint checkerboard matching leaves many coefficient directions outside the nuisance space, and Möbius locking forces logarithmic transverse mass. Allowing all overlapping edges changes the geometry qualitatively: the path differences have only one finite coefficient quotient, and `NB-028` shows that quotient collapses to a Mertens-controlled scalar. The present result shows the corresponding infinite-dimensional endpoint: after the terminal generator tends to zero, even that one-dimensional defect disappears in Hilbert closure.

Therefore **quotienting the entire adjacent family is not a legitimate way to isolate a residual arithmetic subspace**. At infinite scale it annihilates `V_infinity` itself. Any successful spectral separation must be more selective: for example, a scale-dependent low-Rayleigh projector, a quantitatively controlled local packing, or another target-aware decomposition that removes only the universal component while retaining enough of the telescope to reconstruct the target-selected direction.

## 4. Prior-art boundary and adversarial controls

The abstract lemma (20) is elementary Hilbert-space algebra, and no novelty is claimed for it. The Báez-Duarte discrete closure criterion and Bagchi realization are already anchored in `SOURCES.md`; the norm decay (6), adjacent cancellation estimates, Möbius coefficient locking, and endpoint scalar (13) are existing canonical results of this line.

A targeted prior-art check covered the Nyman--Beurling/Báez-Duarte discrete criterion, successive/consecutive differences of the canonical fractional-part generators, finite Gram formulations, and modern work on the Nyman Gram kernel. The search did not locate an explicit published use of the closure identity (4) as an adjacent-mode nuisance obstruction. Search absence is not a priority or novelty proof, and the result is classified `EXACT-DERIVED + NEGATIVE/NUISANCE-QUOTIENT-BOUNDARY`, not as a new theorem of independent literature priority. No new specialized external estimate is load-bearing, so `SOURCES.md` is unchanged.

Several boundaries are essential.

First, (4) is a statement about **closed spans**, not about the low spectral projector of any finite normalized Gram matrix. It does not show that `W_M` equals a low-Rayleigh spectral sector, nor that arbitrary long combinations of adjacent edges have small Hilbert norm. Indeed the telescope that recovers `g_n` is precisely an example where many individually weak local differences cooperate to make an order-one source vector.

Second, individual target angles from `NB-025` cannot be summed without controlling coefficients and Gram interactions. Their decay is compatible with (4); there is no contradiction.

Third, the finite transfer (12) may be badly conditioned when `M` is close to `N`, because `|A_N|` can be large. The near-quadratic enlargement in (17)--(18) is a safe sufficient scale, not a claim of sharpness. Improving that scale would require genuine information about the canonical endpoint coefficient or cancellation in `M(N)`, and an RH-strength Mertens estimate must not be imported as if it were weaker than the desired conclusion.

Fourth, the reformulation of RH using only adjacent differences is logically equivalent to the existing discrete criterion because of (4). It is not evidence for RH and does not satisfy the line objective by itself. Its substantive value is the obstruction it places on the live attempt to identify a universal adjacent subspace and remove it from the source-selected low-Gram geometry.

## 5. Research consequence

The low-spectrum problem after `NB-024`--`NB-028` now has a sharper admissibility condition. The universal adjacent cancellations can be used as **finite, scale-local controls**, but their unrestricted closed span cannot be declared nuisance: it is exactly the full Nyman closure. A useful quotient or preconditioner must therefore retain information about scale, locality, spectral energy, or target loading strongly enough that the long telescope (5) is not silently discarded.

This leaves the genuinely source-specific question intact and better localized. `NB-024` says the canonical target coefficients occupy a low spectral sector when the distance is small; `NB-025`--`NB-026` say a large low-Rayleigh sector exists for universal local reasons; `NB-027` shows Möbius mass escapes either disjoint adjacent matching; `NB-028` shows the full overlapping coefficient quotient collapses; and the present result shows why that collapse is unavoidable at closure level. The next viable separation theorem must act on a **proper scale-dependent subset or spectral image of the adjacent family**, not on the full adjacent span itself.