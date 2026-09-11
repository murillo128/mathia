# PF-288 — diverging local form witnesses force heavy-angle noncompactness

**Status:** `EXACT-DERIVED + FORM-NATIVE-NONCOMPACTNESS-CRITERION + LOCALITY-TO-HEAVY-TRANSFER + ROUTE-SHARPENING`.

[[research/prime_flute/findings/PF-287-heavy-extension-angle-is-exactly-a-product-of-heavy-range-projections|PF-287]] reduces the surviving mixed endpoint to the angle between fixed-strength heavy extension ranges, but its cheapest negative test is still phrased in terms of orthonormal vectors that already lie inside spectral subspaces of `|R_P|` and `|R_H|`. The exact block-Jacobi locality of [[research/prime_flute/findings/PF-214-simultaneous-seam-precision-is-block-jacobi-and-uniform-adjacent-hopping-would-force-exponential-schur-locality|PF-214]] removes that spectral-construction burden for a large class of physical tests.

Suppose one can build pairwise separated local physical-low/high form vectors `u_j,v_j` whose diagonal extension energies dominate their Hilbert norms,

\[
\frac{k[u_j]}{\|u_j\|^2}\to\infty,
\qquad
\frac{k[v_j]}{\|v_j\|^2}\to\infty,
\]

while their energy-normalized mixed correlation stays bounded away from zero,

\[
\frac{|k[u_j,v_j]|}
{\sqrt{k[u_j]k[v_j]}}
\ge c>0.
\]

Then the PF-287 heavy angle is noncompact at **every fixed positive strength threshold**, and therefore the PF-281/PF-282 mixed operator `T` is noncompact. The proof is elementary but useful: normalize each local vector by its diagonal form energy, observe that divergent Rayleigh quotient pushes the normalized vector asymptotically into every fixed heavy spectral sector, then pass to a sparse subsequence so the low-strength tails form an arbitrarily small Hilbert--Schmidt synthesis error. PF-214 locality makes the unprojected cross-Gram matrix exactly diagonal. The projected heavy families can then be re-orthonormalized without destroying the uniform diagonal correlation.

Equivalently, **compactness of the physical mixed operator forces every such separated high-energy local low/high family to become asymptotically energy-orthogonal**. This converts PF-287's global heavy-spectral falsifier into a local form test on repeated pant windows.

For the canonical Prime-Flute split, PF-216 already supplies the low half of this test: the tangentially constant physical-low module vector has Rayleigh quotient `\gtrsim P_n/\log P_n\to\infty`. The remaining negative gate is therefore sharply local: find a pairwise separated physical-high local family with diverging diagonal Rayleigh quotient and prove that its normalized mixed form correlation with the PF-216 low family does not vanish. This finding does **not** assert that such a high family or nonvanishing mixed correlation exists.

## Claim

Retain the PF-281/PF-282 abstract form setting. Let

\[
\mathcal H=\mathcal H_P\oplus\mathcal H_H
\]

with physical projections `P,H`, and let `k` be the closed nonnegative precision form with canonical energy map

\[
R=K^{1/2},
\qquad
R_P=R|_{P\operatorname{Dom}k},
\qquad
R_H=R|_{H\operatorname{Dom}k}.
\]

Thus

\[
k[u]=\|R_Pu\|^2=\||R_P|u\|^2
\quad(u\in P\operatorname{Dom}k),
\]

and similarly on the `H` side. Let

\[
\Gamma=V_P^*V_H
\]

be the PF-282 extension angle.

Assume the physical module decomposition is such that the form is nearest-neighbor in module index as in PF-214. Let `I_j` be finite module windows satisfying

\[
\operatorname{dist}(I_i,I_j)>1
\qquad(i\ne j),
\tag{1}
\]

and choose nonzero vectors

\[
u_j\in P\operatorname{Dom}k,
\qquad
v_j\in H\operatorname{Dom}k
\]

supported in `I_j`. Put

\[
a_j:=k[u_j],
\qquad
b_j:=k[v_j].
\tag{2}
\]

Suppose

\[
\boxed{
\frac{a_j}{\|u_j\|^2}\to\infty,
\qquad
\frac{b_j}{\|v_j\|^2}\to\infty,
}
\tag{3}
\]

and for some fixed `c>0`, after passing to a tail if necessary,

\[
\boxed{
|k[u_j,v_j]|\ge c\sqrt{a_jb_j}.
}
\tag{4}
\]

Then, for every fixed `\mu>0`, with

\[
E_P^\mu=\mathbf1_{[\mu,\infty)}(|R_P|),
\qquad
E_H^\mu=\mathbf1_{[\mu,\infty)}(|R_H|),
\tag{5}
\]

the heavy angle

\[
E_P^\mu\Gamma E_H^\mu
\tag{6}
\]

is noncompact. Consequently the PF-282 mixed operator

\[
T=f(|R_P|)\Gamma f(|R_H|),
\qquad
f(t)=\frac{t}{\sqrt{1+t^2}},
\tag{7}
\]

is noncompact and therefore cannot belong to `\mathcal S_{1,\infty}`.

The contrapositive is the operational statement:

\[
\boxed{
T\text{ compact}
\Longrightarrow
\frac{k[u_j,v_j]}{\sqrt{k[u_j]k[v_j]}}\to0
}
\tag{8}
\]

for every separated local pair family satisfying the two divergent Rayleigh conditions (3).

## 1. Locality makes the energy-normalized families exactly orthonormal

Define

\[
x_j:=\frac{|R_P|u_j}{\sqrt{a_j}},
\qquad
y_j:=\frac{|R_H|v_j}{\sqrt{b_j}}.
\tag{9}
\]

Then `\|x_j\|=\|y_j\|=1`. Because PF-214 gives nearest-neighbor form support and the combined support windows satisfy (1), for `i\ne j`,

\[
k[u_i,u_j]=k[v_i,v_j]=k[u_i,v_j]=0.
\tag{10}
\]

Hence

\[
\langle x_i,x_j\rangle
=\frac{k[u_i,u_j]}{\sqrt{a_ia_j}}
=0,
\qquad
\langle y_i,y_j\rangle=0.
\tag{11}
\]

Thus `(x_j)` and `(y_j)` are orthonormal families. PF-282's energy-factorization identity gives, for all `i,j`,

\[
\langle x_i,\Gamma y_j\rangle
=
\frac{k[u_i,v_j]}{\sqrt{a_i b_j}}.
\tag{12}
\]

By (10), the cross-Gram matrix is exactly diagonal:

\[
D:=X^*\Gamma Y
=\operatorname{diag}(\gamma_j),
\qquad
\gamma_j:=\frac{k[u_j,v_j]}{\sqrt{a_jb_j}},
\tag{13}
\]

where `X,Y:\ell^2\to\mathcal H` are the isometries with columns `x_j,y_j`. Assumption (4) says

\[
\boxed{|\gamma_j|\ge c.}
\tag{14}
\]

So before spectral thresholding the local form witnesses already give an infinite diagonal angle bounded away from zero.

## 2. Divergent Rayleigh quotient pushes unit-energy vectors into every fixed heavy sector

Fix `\mu>0`. For the low side let

\[
Q_P:=E_P^\mu,
\qquad
x_j^{<}:=(I-Q_P)x_j.
\]

By the spectral theorem,

\[
\begin{aligned}
\|x_j^{<}\|^2
&=
\frac1{a_j}
\left\|
\mathbf1_{[0,\mu)}(|R_P|)|R_P|u_j
\right\|^2\\
&\le
\frac{\mu^2\|u_j\|^2}{a_j}.
\end{aligned}
\tag{15}
\]

Equation (3) therefore implies

\[
\boxed{\|x_j^{<}\|\to0.}
\tag{16}
\]

Exactly the same argument gives, with `Q_H=E_H^\mu`,

\[
\boxed{
\|(I-Q_H)y_j\|^2
\le
\frac{\mu^2\|v_j\|^2}{b_j}
\to0.
}
\tag{17}
\]

This is the key local-to-heavy transfer. One does not need to construct spectral vectors directly. If a local vector has diagonal form energy much larger than its Hilbert mass, its **unit-energy image** is asymptotically supported above every fixed strength threshold.

## 3. A sparse subsequence turns the asymptotic heavy property into an infinite heavy witness

Let `\varepsilon>0`. From (16)--(17), pass to a common subsequence, still indexed by `j`, such that

\[
\sum_j\|(I-Q_P)x_j\|^2<\varepsilon^2,
\qquad
\sum_j\|(I-Q_H)y_j\|^2<\varepsilon^2.
\tag{18}
\]

Set

\[
X_h:=Q_PX,
\qquad
Y_h:=Q_HY,
\qquad
E:=(I-Q_P)X,
\qquad
F:=(I-Q_H)Y.
\tag{19}
\]

Equation (18) gives Hilbert--Schmidt, hence operator-norm, control

\[
\|E\|\le\varepsilon,
\qquad
\|F\|\le\varepsilon.
\tag{20}
\]

Since `X,Y` are isometries,

\[
A:=X_h^*X_h=I-E^*E,
\qquad
B:=Y_h^*Y_h=I-F^*F,
\tag{21}
\]

so for `\varepsilon<1`,

\[
(1-\varepsilon^2)I\le A,B\le I.
\tag{22}
\]

The projected cross matrix

\[
M:=X_h^*\Gamma Y_h
\tag{23}
\]

differs from the exact diagonal matrix (13) by at most

\[
\boxed{
\|M-D\|
\le 2\varepsilon+\varepsilon^2,
}
\tag{24}
\]

because `\|\Gamma\|\le1` and

\[
D-M
=E^*\Gamma Y_h+X_h^*\Gamma F+E^*\Gamma F.
\]

Choose `\varepsilon` so small that

\[
2\varepsilon+\varepsilon^2<c/2.
\tag{25}
\]

Then (14) and (24) imply

\[
\boxed{\|Mz\|\ge(c/2)\|z\|\qquad(z\in\ell^2).}
\tag{26}
\]

Now orthonormalize inside the fixed heavy sectors by defining

\[
U:=X_hA^{-1/2},
\qquad
V:=Y_hB^{-1/2}.
\tag{27}
\]

Equations (21)--(22) show that `U,V` are isometries with

\[
\operatorname{Ran}U\subset\operatorname{Ran}Q_P,
\qquad
\operatorname{Ran}V\subset\operatorname{Ran}Q_H.
\tag{28}
\]

Their heavy cross-Gram operator is

\[
U^*\Gamma V=A^{-1/2}MB^{-1/2}.
\tag{29}
\]

Because `A,B\le I`, both `A^{-1/2}` and `B^{-1/2}` have lower bound one. Combining with (26),

\[
\boxed{
\|U^*\Gamma V z\|
\ge(c/2)\|z\|.
}
\tag{30}
\]

Thus the compression of `Q_P\Gamma Q_H` to two infinite-dimensional heavy subspaces is bounded below. It cannot be compact. Since `\mu>0` was arbitrary, every fixed positive heavy threshold carries a noncompact angle.

PF-282 then implies that `T` is noncompact: on any fixed heavy sector the strength factors `f(|R_P|),f(|R_H|)` are boundedly invertible on their ranges, so a noncompact heavy angle cannot be regularized by them.

## 4. Prime-Flute specialization: one half of the local falsifier already exists

PF-216 gives a canonical physical-low vector on the `n`th seam module,

\[
\ell_n
=\frac{\Lambda_{Q,n}^{1/2}\mathbf1_n}{\sqrt{q_n}},
\qquad
\|\ell_n\|=1,
\tag{31}
\]

with zero physical tangential frequency. It lies in the PF-212 low sector and satisfies

\[
\boxed{
k[\ell_n]\gtrsim q_n^{-1}
\asymp\frac{P_n}{\log P_n}\to\infty.}
\tag{32}
\]

Taking a sparse module subsequence supplies the support separation (1). Therefore the first Rayleigh condition in (3) is already available on a completely explicit one-dimensional local channel.

The current negative test for the heavy-angle problem can consequently be stated without spectral projectors:

- choose a local physical-high vector `h_n` (or a uniformly finite-dimensional local high family) on the same sparse pant windows;
- prove `k[h_n]/\|h_n\|^2\to\infty`;
- prove
  \[
  \frac{|k[\ell_n,h_n]|}
  {\sqrt{k[\ell_n]k[h_n]}}
  \not\to0.
  \tag{33}
  \]

If these three local statements hold along one sparse tail, the mixed operator is noncompact by the theorem above.

PF-227 does **not** already supply (33). Its inverse-seam multiplicity theorem concerns the raw physical high/high crossing and deliberately does not identify the low/high extension angle. Likewise PF-286 proves that the physical high strength factor is noncompact, but does not localize a diverging high Rayleigh sequence with persistent correlation to (31). Those are genuine remaining geometric obligations.

## 5. Why this is stronger operationally than the PF-287 finite witness test

PF-287's negative criterion asks for arbitrary-dimensional orthonormal families already lying in fixed heavy spectral ranges and having a uniformly invertible cross-energy Gram matrix. That criterion is exact but can be awkward in the physical geometry because spectral projection by `|R_P|` or `|R_H|` is global.

The present result replaces that construction by three local quantities: diagonal low energy, diagonal high energy, and mixed energy on spatially separated windows. The heavy spectral projection is performed only in the proof. Divergent local Rayleigh quotients guarantee that it removes asymptotically negligible mass, while PF-214 makes different windows exactly form-orthogonal before projection. A sparse subsequence absorbs the residual spectral tails.

This is also why the theorem needs **divergence**, not merely a uniform lower bound, for both diagonal Rayleigh quotients. A fixed lower bound does not force the unit-energy vectors into an arbitrarily prescribed positive heavy sector, and the projection error in (15)--(17) need not vanish.

## 6. Prior art and novelty audit

The Hilbert-space ingredients are classical. Spectral projections, the characterization of compactness by infinite orthonormal families, polar decomposition, and products of projections are standard; PF-287 already audits the principal-angle and essential-orthogonality literature, including Galántai and Andruchow--Corach. No novelty is claimed for those general facts, nor for passing to a subsequence whose norm-null errors are square summable.

A targeted audit of essential-orthogonality/principal-angle literature and compact-operator sequence criteria did not identify a distinct general theorem that should replace the elementary proof above. The abstract lemma should nevertheless be regarded as a direct Hilbert-space consequence, not as a new general operator theorem.

The durable project-specific contribution is the **PF-locality bridge**: PF-214's exact block-Jacobi form support plus divergent physical diagonal Rayleigh energy is enough to manufacture the fixed-heavy spectral witnesses demanded by PF-287. This changes the next research obligation from constructing global heavy spectral vectors to estimating a local normalized low/high form correlation on repeated pant windows.

## 7. Boundaries and falsification discipline

The conclusion requires both Rayleigh quotients in (3) to diverge. PF-216 supplies this only on the low side. PF-286's noncompact high strength is not, by itself, the local high-Rayleigh hypothesis used here.

The support separation is also load-bearing. It is what makes the unprojected cross-Gram matrix diagonal in (13). For overlapping or merely weakly coupled windows, additional off-diagonal control would be required.

Equation (4) is an **energy-normalized** mixed lower bound. A large raw DtN crossing or many raw high/high channels does not imply it. In particular PF-226/PF-227 cannot be substituted for (4) without a new calculation involving the actual physical `P/H` split.

Conversely, failure to find a family satisfying (3)--(4) is not evidence that the heavy angle is compact. Compactness still requires the full PF-287 orthonormal-sequence condition at every fixed threshold. The theorem is a sufficient noncompactness certificate, not a positive criterion.

Nothing here proves the weak-trace endpoint, a wave-operator theorem, trace formula, relative determinant, prime/clone separation, zeta-zero correspondence, critical-line statement, or RH consequence.