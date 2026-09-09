# NB-004 — fixed semigroup target probes admit target-orthogonal Mellin aliases

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + COMPRESSED-EIGENSPACE-REDUCTION + APPROXIMATE-SPECTRAL-ALIASING + NEGATIVE/OBSTRUCTION`. Bagchi's integer dilation semigroup supplies an exact target character inside the canonical discrete Nyman space, but a fixed finite set of adjoint-semigroup tests cannot select that target quantitatively. For every fixed finite set of integer scales `S`, there are unit vectors in the canonical space, exactly orthogonal to the Nyman target, whose target-character defects tend to zero simultaneously at every scale in `S`.

The result does **not** assert that the target is the unique exact common eigenvector of the compressed adjoints. That stronger statement does not follow merely from the corresponding full-space uniqueness because the discrete Nyman space is invariant but not known to be reducing for the dilation operators. Reopening the compression directly gives an exact coordinate characterization: common target-character eigenvectors for scales `2` and `3` are equivalent to finite-energy sequences `c_n` satisfying `c_{2n}=c_{3n}=c_n`. The constant sequence gives the target; whether the finite-energy condition forces every such invariant sequence to be constant is a separate rigidity problem and is not needed for the quantitative obstruction below.

Thus the durable negative statement is stronger than a failure of one proof of exact uniqueness and weaker than the withdrawn claim: **regardless of the exact joint eigenspace, finite semigroup covariance defects have no modulus that controls distance to the fixed target direction.** Any positive semigroup-based certificate must either use a scale family growing with the section together with an anti-aliasing theorem, restrict the admitted Mellin-frequency content independently, or retain the target pairings themselves.

## 1. Canonical discrete dilation and the fixed target character

Let `\mathcal M` be Bagchi's closed subspace of `L^2((0,1])` consisting of functions constant on the harmonic intervals

\[
I_n=\left(\frac1{n+1},\frac1n\right],\qquad n\ge1.
\]

For an integer `m\ge1`, Bagchi defines the isometry

\[
(T_mf)(x)=
\begin{cases}
\sqrt m\,f(mx),&0<x\le1/m,\\
0,&1/m<x\le1.
\end{cases}
\tag{1}
\]

and `T_m\mathcal M\subseteq\mathcal M`. Write `A_m=T_m|_{\mathcal M}` and let

\[
e(x)=1.
\]

For every `f\in\mathcal M`, direct integration gives

\[
\langle f,A_m^*e\rangle
=\langle A_mf,e\rangle
=\frac1{\sqrt m}\langle f,e\rangle.
\]

Hence

\[
\boxed{A_m^*e=m^{-1/2}e.}
\tag{2}
\]

This is the exact target-sensitive covariance already suggested by `NB-002`: the global target transforms with the absolute multiplicative character `m^{-1/2}`.

On the full space `L^2((0,1])`, the adjoint is

\[
\boxed{(T_m^*h)(y)=m^{-1/2}h(y/m).}
\tag{3}
\]

The full-space equations at scales `2` and `3` force a measurable solution to be constant, because they become invariance under translations by `\log2` and `\log3` after the change of variables `y=e^{-t}`. But this does **not** transfer automatically to `A_m^*`: for an invariant subspace,

\[
A_m^*=P_{\mathcal M}T_m^*|_{\mathcal M},
\tag{4}
\]

and equality with the full adjoint restriction would require a reducing property not supplied by Bagchi's semigroup construction.

## 2. The exact compressed target eigenspace reduces to a finite-energy multiplicative invariance problem

The compression can be analyzed without any reducing assumption. Put

\[
\Phi_n=\mathbf 1_{(0,1/n]},\qquad n\ge1.
\tag{5}
\]

The vectors `\Phi_n` are total in `\mathcal M`, since

\[
\Phi_n-\Phi_{n+1}=\mathbf1_{I_n}.
\]

Equation (1) gives exactly

\[
\boxed{T_m\Phi_n=\sqrt m\,\Phi_{mn}.}
\tag{6}
\]

Let `h\in\mathcal M` and define

\[
F_n:=\langle h,\Phi_n\rangle
=\int_0^{1/n}h(x)\,dx,
\qquad
c_n:=nF_n.
\tag{7}
\]

Using totality and (6),

\[
A_m^*h=m^{-1/2}h
\]

is equivalent to

\[
\sqrt m\,F_{mn}=m^{-1/2}F_n
\qquad(n\ge1),
\]

or

\[
\boxed{c_{mn}=c_n\qquad(n\ge1).}
\tag{8}
\]

Consequently the exact two-scale target-character space is characterized by

\[
\boxed{c_{2n}=c_n,\qquad c_{3n}=c_n\qquad(n\ge1).}
\tag{9}
\]

This condition is also sufficient: if (9) holds for the sequence extracted from `h`, then the adjoint equations hold against the total family `\{\Phi_n\}` and hence on all of `\mathcal M`.

The Hilbert-space constraint can be written entirely in the same coordinates. If `h_n` is the value of `h` on `I_n`, then

\[
F_n-F_{n+1}=\frac{h_n}{n(n+1)},
\]

so (7) gives

\[
\boxed{h_n=(n+1)c_n-nc_{n+1}.}
\tag{10}
\]

Therefore common target-character eigenvectors for `A_2^*,A_3^*` correspond exactly to invariant sequences satisfying

\[
\boxed{
\sum_{n\ge1}
\frac{|(n+1)c_n-nc_{n+1}|^2}{n(n+1)}<\infty.
}
\tag{11}
\]

The constant sequence `c_n=C` gives `h_n=C`, hence `\mathbb Ce` lies in the exact joint eigenspace. What is **not** established here is the converse implication from (9)--(11) to constancy. This is the precise missing lemma behind the withdrawn compressed-uniqueness claim; no full-space argument substitutes for it.

## 3. Projected Mellin characters remain exact compressed eigencharacters

The quantitative obstruction does not require resolving (9)--(11). For real `\tau`, set

\[
h_\tau(x)=x^{i\tau},\qquad \|h_\tau\|_2=1,
\tag{12}
\]

and let `P_{\mathcal M}` be orthogonal projection onto `\mathcal M`. Equation (3) gives

\[
T_m^*h_\tau=m^{-1/2-i\tau}h_\tau.
\tag{13}
\]

Define

\[
v_\tau=P_{\mathcal M}h_\tau.
\tag{14}
\]

For `f\in\mathcal M`, invariance of `\mathcal M` under `T_m` gives

\[
\begin{aligned}
\langle f,A_m^*v_\tau\rangle
&=\langle T_mf,v_\tau\rangle\\
&=\langle T_mf,h_\tau\rangle\\
&=\langle f,T_m^*h_\tau\rangle\\
&=m^{-1/2-i\tau}\langle f,v_\tau\rangle.
\end{aligned}
\]

Thus

\[
\boxed{A_m^*v_\tau=m^{-1/2-i\tau}v_\tau\qquad(m\ge1).}
\tag{15}
\]

This projection step is valid precisely because it is proved through inner products with `T_mf\in\mathcal M`; it does not assert that `T_m^*` preserves `\mathcal M`.

The vectors `v_\tau` are nonzero and retain a controlled amount of norm. On `I_n`, the phase of `x^{i\tau}` varies by at most

\[
|\tau|\log\frac{n+1}{n}\le\frac{|\tau|}{n}.
\]

For `|\tau|\ge1` and

\[
N_\tau=\lceil2|\tau|\rceil,
\]

the conditional average on every `I_n`, `n\ge N_\tau`, therefore has modulus at least `\cos(1/4)`. Since the union of those intervals is `(0,1/N_\tau]`,

\[
\boxed{
\|v_\tau\|_2^2
\ge
\frac{\cos^2(1/4)}{\lceil2|\tau|\rceil}.
}
\tag{16}
\]

Projection also preserves the target pairing because `e\in\mathcal M`:

\[
\boxed{
\langle v_\tau,e\rangle
=\int_0^1x^{i\tau}\,dx
=\frac1{1+i\tau}.
}
\tag{17}
\]

After normalization `u_\tau=v_\tau/\|v_\tau\|`, (16)--(17) imply

\[
|\langle u_\tau,e\rangle|=O(|\tau|^{-1/2}),
\qquad
\boxed{
\operatorname{dist}(u_\tau,\mathbb Ce)\to1.
}
\tag{18}
\]

## 4. Every fixed finite scale family has target-orthogonal approximate aliases

From (15), the target-character defect is exact:

\[
\boxed{
\|(A_m^*-m^{-1/2}I)u_\tau\|
=m^{-1/2}|m^{-i\tau}-1|.
}
\tag{19}
\]

Let `S=\{m_1,\ldots,m_r\}` be any fixed finite set of positive integer scales. Simultaneous Diophantine approximation applied to

\[
\left(\frac{\log m_1}{2\pi},\ldots,
      \frac{\log m_r}{2\pi}\right)
\]

produces an unbounded sequence `\tau_j` for which

\[
\boxed{m_\ell^{-i\tau_j}\to1
\qquad(1\le\ell\le r).}
\tag{20}
\]

For the pair `2,3`, one may see this explicitly by taking continued-fraction convergents `p_j/q_j` to `\log3/\log2` and

\[
\tau_j=\frac{2\pi q_j}{\log2};
\]

then `2^{-i\tau_j}=1` exactly and `3^{-i\tau_j}\to1`.

To place the aliases exactly in the target-orthogonal complement, write

\[
a_\tau=\langle u_\tau,e\rangle,
\qquad
w_\tau=
\frac{u_\tau-a_\tau e}{\sqrt{1-|a_\tau|^2}}.
\tag{21}
\]

For large `|\tau|`, this is a unit vector in `\mathcal M\cap e^\perp`. Because the target itself satisfies (2), subtracting its component does not change any semigroup defect except for the normalization factor:

\[
\boxed{
\|(A_m^*-m^{-1/2}I)w_\tau\|
=
\frac{m^{-1/2}|m^{-i\tau}-1|}
     {\sqrt{1-|a_\tau|^2}}.
}
\tag{22}
\]

Combining (18), (20), and (22) yields

\[
\boxed{
\inf_{\substack{w\in\mathcal M\cap e^\perp\\\|w\|=1}}
\max_{m\in S}
\|(A_m^*-m^{-1/2}I)w\|=0.
}
\tag{23}
\]

This conclusion is independent of the unresolved exact eigenspace classification. In particular, there is no function `\omega_S(\varepsilon)\to0` such that every unit `u\in\mathcal M` obeys

\[
\boxed{
\operatorname{dist}(u,\mathbb Ce)
\le
\omega_S\!\left(
\max_{m\in S}\|(A_m^*-m^{-1/2}I)u\|
\right).
}
\tag{24}
\]

Indeed `w_{\tau_j}` makes the argument of `\omega_S` tend to zero while the left side is identically one.

## 5. Consequence for target-aware finite-section certificates

`NB-001` proves that the finite Nyman distance is controlled by augmented Gram data, not generator Gram geometry alone. `NB-002` then shows that canonical multiplicative copies preserve local Gram blocks while diluting fixed-target capture by the exact factor `1/m`. The present result closes another natural compression attempt: replacing explicit target pairings by finitely many fixed semigroup-covariance probes.

The obstruction is ordinary Mellin aliasing. The full Mellin character `x^{i\tau}` is an exact dilation eigencharacter, its projection into Bagchi's canonical discrete space remains an exact **compressed** eigencharacter, and high vertical frequencies can return arbitrarily close to the target phases on any finite set of logarithmic samples. Orthogonalizing against the target leaves this recurrence intact.

A positive semigroup route therefore needs more information than a fixed finite probe set. Three possibilities remain mathematically distinct:

1. let the sampled scale set grow with the finite Nyman section and prove a quantitative anti-aliasing theorem on the admitted vertical-frequency range;
2. derive an independent source theorem restricting the Mellin-frequency content of actual near-optimal residuals or coefficient families;
3. retain the canonical target-pairing vector, or an equivalent normed primal/dual datum, rather than trying to infer it from scale covariance.

Equation (23) does not estimate the actual approximation distance `d_N`, and it does not say that high-frequency aliases arise as residuals of best finite Nyman approximants. Those are additional source-selection obligations.

## 6. Prior art, correction boundary, and audit

The load-bearing external input is Bhaskar Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, Proc. Indian Acad. Sci. Math. Sci. 116 (2006), 137--146; arXiv:math/0607733. Bagchi defines `\mathcal M`, the isometries `T_m`, their semigroup law, and their action on the canonical discrete generators. The adjoint formula (3), the projected-eigencharacter identity (15), and the coordinate reduction (7)--(11) are elementary Hilbert-space consequences reconstructed here.

The recurrence in (20) is classical simultaneous Diophantine approximation; the two-scale specialization is ordinary continued-fraction approximation. A targeted literature search did not identify the specific projected-Mellin aliasing statement (23) as a named Nyman--Beurling theorem. That absence is not a novelty claim: the mechanism is assembled from classical dilation covariance, orthogonal projection, and torus recurrence.

The key correction boundary is explicit. Full-space uniqueness under the two periods `\log2,\log3` is valid, but the implication to the compressed adjoints is not justified by invariance of `\mathcal M`. The exact compressed problem is (9)--(11). This finding deliberately leaves that rigidity question open and does not use it in (23)--(24).

The result is unconditional and concerns the canonical Hilbert space, but it is only an **information/stability obstruction**. It proves neither RH nor its negation, gives no new Nyman approximation rate, and does not improve Burnol's zero-sensitive lower-bound scale. Its durable content is that finite fixed semigroup target probes cannot replace the target-aware data required by the finite-section problem.