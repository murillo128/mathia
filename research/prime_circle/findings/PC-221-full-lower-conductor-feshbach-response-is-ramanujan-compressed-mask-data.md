# PC-221 — full lower-conductor Feshbach response is Ramanujan-compressed mask data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the most canonical collective escape left open by PC-220: do not inspect only the fixed-level compression `T_n=P_nM_{g_n}P_n`, but retain its coupling to **all proper exact-order conductor sectors at once**, and ask whether direct leakage or exact Schur/Feshbach elimination creates an independent cross-level spectral carrier.

It does not. The direct top-to-lower leakage has an exact and mildly striking zero set:

\[
\boxed{(I-P_n)M_{g_n}P_n=0
\iff n\text{ is a prime power}.}
\tag{1}
\]

This is not a new prime-power mechanism. It is precisely the elementary local-ring property of `Z/nZ`: the Fourier transform of the cyclotomic coefficient mask vanishes exactly on the units, and a unit plus a nonunit is always a unit exactly when `Z/nZ` is local, equivalently when `n=p^r`. Thus (1) recovers only the support already selected by the common-anchor von Mangoldt identity.

For mixed conductors the leakage is genuinely nonzero, but its **entire singular spectrum** still reduces to the cyclotomic coefficient diagonal together with the standard Ramanujan exact-order projector. More strongly, integrating out every proper conductor nonperturbatively gives a Feshbach response whose inverse is merely the exact-order compression of the scalar resolvent `(z-g_n)^{-1}`. Hence the complete unweighted lower-conductor sector introduces no additional primitive-root phase, connection, monodromy, spectral scale, or critical-line structure beyond finite cyclotomic coefficient data under a classical Fourier/Ramanujan projection.

## 1. Canonical all-lower-conductor split

Work first at one conductor `n>1` in

\[
\mathcal H_n=L^2(\mathbb Z/n\mathbb Z)
\]

with normalized counting measure. PC-066 gives the orthogonal exact-order decomposition

\[
\boxed{
\mathcal H_n=\bigoplus_{d\mid n}E_d,
}
\tag{2}
\]

where `E_d` is the span of Fourier characters of exact order `d` and `P_d` is the corresponding Ramanujan projector. Put

\[
P:=P_n,
\qquad
Q:=I-P=\sum_{\substack{d\mid n\\d<n}}P_d.
\tag{3}
\]

Thus `P` is the primitive/new transverse sector and `Q` is **all lower conductor sectors together**. No divisor weight, ordering, or externally chosen transform has been inserted.

Retain the normalized coefficient mask of PC-212,

\[
\Phi_n(z)=\sum_{r=0}^{n-1}a_n(r)z^r,
\qquad
h_n:=\sum_{r=0}^{n-1}a_n(r)^2,
\qquad
 g_n(r):=\sqrt{\frac n{h_n}}\,a_n(r),
\tag{4}
\]

zero-padding the coefficient vector to length `n`. Let

\[
M:=M_{g_n}
\]

be multiplication by this real cylinder function. PC-220 studies

\[
T_n=PMP\big|_{E_n}.
\tag{5}
\]

The canonical cross-level object before discarding the lower sectors is instead the leakage map

\[
\boxed{
L_n:=QMP:E_n\longrightarrow Q\mathcal H_n.
}
\tag{6}
\]

It contains simultaneously every block `P_dM_{g_n}P_n`, `d|n`, `d<n`.

## 2. The leakage vanishes exactly for prime powers

Let `zeta_n=e^{2pi i/n}`. With the normalized Fourier convention on `Z/nZ`, equation (4) gives

\[
\boxed{
\widehat g_n(k)
=\frac{\Phi_n(\zeta_n^{-k})}{\sqrt{nh_n}}.
}
\tag{7}
\]

The roots of `Phi_n` are exactly the primitive `n`-th roots. Therefore

\[
\boxed{
\widehat g_n(k)=0
\iff (k,n)=1.
}
\tag{8}
\]

So the Fourier support of `g_n` is not merely contained in lower conductors: it is **exactly the set of nonunits of `Z/nZ`**.

In the Fourier basis, a matrix entry of (6) from an input unit frequency `beta in U(n)` to an output nonunit frequency `alpha notin U(n)` is

\[
\boxed{
(L_n)_{\alpha,\beta}
=\widehat g_n(\alpha-\beta).
}
\tag{9}
\]

By (8), `L_n=0` if and only if

\[
\alpha\notin U(n),\ \beta\in U(n)
\quad\Longrightarrow\quad
\alpha-\beta\in U(n).
\tag{10}
\]

If `n=p^r`, every nonunit is divisible by `p`, while every unit is nonzero modulo `p`; hence `alpha-beta` is nonzero modulo `p` and is a unit. Thus `L_{p^r}=0`.

Conversely, suppose two distinct primes `p,q` divide `n`. By CRT choose `alpha mod n` with

\[
\alpha\equiv0\pmod p,
\qquad
\alpha\equiv1\pmod q,
\tag{11}
\]

and take `beta=1`. Then `alpha` is a nonunit and `alpha-beta` is also a nonunit, so (8)--(9) give a nonzero leakage entry. This proves (1).

Algebraically, (10) is the familiar statement that adding a nonunit to a unit stays a unit. For `Z/nZ` this holds exactly when the nonunits form the unique maximal ideal, i.e. exactly when `Z/nZ` is local, equivalently `n` is a prime power. Hence the operator criterion is a geometric/Fourier realization of a textbook ring-theoretic dichotomy, not new arithmetic.

It also has a direct Prime-Circle control:

\[
\boxed{
L_n=0
\iff n=p^r
\iff \Lambda(n)>0
\qquad(n>1).
}
\tag{12}
\]

Thus the zero/nonzero pattern of the collective transverse leakage recovers the **support** of the exact common-anchor von Mangoldt observable PC-001, but not its `log p` magnitude or any new zero-sensitive datum.

## 3. The complete leakage singular spectrum is fixed-level Ramanujan data

The mixed-conductor case is not spectrally empty. Nevertheless its entire all-lower leakage spectrum can be reduced exactly to the same classical data isolated by PC-220.

Let

\[
S_n:=\{r:a_n(r)\ne0\},
\]

and use the PC-220 matrices

\[
A_n=(\zeta_n^{ru})_{r\in S_n,\ u\in U(n)},
\qquad
D_n:=\operatorname{diag}(a_n(r))_{r\in S_n},
\qquad
C_n:=A_nA_n^*.
\tag{13}
\]

Then

\[
(C_n)_{r,s}=c_n(r-s),
\tag{14}
\]

so `C_n/n` is the principal compression of the standard exact-order Ramanujan/Fourier projector. PC-220 gives

\[
T_n=\frac1{\sqrt{nh_n}}A_n^*D_nA_n.
\tag{15}
\]

Since `M` is self-adjoint,

\[
\begin{aligned}
L_n^*L_n
&=PMQMP\\
&=PM^2P-(PMP)^2.
\end{aligned}
\tag{16}
\]

The first term is just the same Fourier compression with the coefficient profile squared:

\[
PM^2P
=\frac1{h_n}A_n^*D_n^2A_n.
\tag{17}
\]

Combining (15)--(17) and `C_n=A_nA_n^*` yields

\[
\boxed{
L_n^*L_n
=\frac1{nh_n}
A_n^*D_n(nI-C_n)D_nA_n.
}
\tag{18}
\]

Because `C_n/n` is a principal compression of an orthogonal projector, `0<=C_n<=nI`. Put

\[
X_n:=(nI-C_n)^{1/2}D_nA_n.
\]

Then `nh_n L_n^*L_n=X_n^*X_n`, and the `XY/YX` transfer gives the exact support-space singular-spectrum formula

\[
\boxed{
\operatorname{Spec}^{\times}(nh_nL_n^*L_n)
=
\operatorname{Spec}^{\times}
\!\left(
(nI-C_n)^{1/2}D_nC_nD_n(nI-C_n)^{1/2}
\right).
}
\tag{19}
\]

Thus even though `L_n` explicitly couples the primitive sector to **every proper conductor sector**, all of its singular values are determined by two finite ingredients already classicalized in PC-220: the ordinary cyclotomic coefficient diagonal `D_n` and the Ramanujan/gcd kernel `C_n`.

Exact small controls illustrate both sides. For `n=4`, `Phi_4(z)=1+z^2` and (1) gives `L_4=0`. For the first mixed conductor `n=6`, `Phi_6(z)=1-z+z^2`, `h_6=3`, and (19) gives

\[
\boxed{
\operatorname{Spec}(L_6^*L_6)
=\left\{\frac{17}{18},\frac12\right\}.
}
\tag{20}
\]

So the mixed-conductor leakage is large and genuinely operator-valued; the negative result is not that the coupling vanishes, but that its complete unweighted singular data remain inside the coefficient/Ramanujan package.

## 4. Exact Feshbach elimination adds no hidden lower-sector dynamics

A stronger test is to retain the lower-conductor sector nonperturbatively rather than replace it by the quadratic leakage (18).

For `z` in a common resolvent domain, define the exact lower-sector self-energy

\[
\Sigma_n(z)
:=PMQ\,(zQ-QMQ)^{-1}QMP
\tag{21}
\]

and the Feshbach/Schur operator on `E_n`

\[
F_n(z)
:=zP-T_n-\Sigma_n(z).
\tag{22}
\]

The standard Schur-complement identity gives

\[
\boxed{
F_n(z)^{-1}
=P(zI-M)^{-1}P.
}
\tag{23}
\]

But the full operator `M` is multiplication in the coefficient/vertex coordinate. Let

\[
\mathcal A_n=(\zeta_n^{ru})_{0\le r<n,\ u\in U(n)}.
\tag{24}
\]

Then (23) has the explicit finite formula

\[
\boxed{
F_n(z)^{-1}
=\frac1n\mathcal A_n^*
\operatorname{diag}\!\left(
\frac1{z-\sqrt{n/h_n}\,a_n(r)}
\right)_{0\le r<n}
\mathcal A_n.
}
\tag{25}
\]

The full row Gram matrix of `mathcal A_n` is again the standard Ramanujan kernel,

\[
(\mathcal A_n\mathcal A_n^*)_{r,s}=c_n(r-s).
\tag{26}
\]

Equation (25) is the decisive collapse: after **all** proper exact-order conductors have been integrated out exactly, the resulting energy-dependent response is merely the exact-order Fourier compression of a pointwise rational function of the finite cyclotomic coefficient profile.

More generally, for every scalar function `f` defined on the finite spectrum of `M`,

\[
\boxed{
P f(M)P
=\frac1n\mathcal A_n^*
\operatorname{diag}\bigl(f(g_n(r))\bigr)
\mathcal A_n.
}
\tag{27}
\]

So the collective lower-conductor excursions do not generate a new connection or spectral variable. They reorganize ordinary scalar functional calculus of the coefficient mask through the already-known exact-order Ramanujan projector.

## 5. Fully summed conductor paths are only insertions of the identity

The same obstruction persists for finite words. Because the exact-order projectors resolve the identity as in (2), for multiplication operators `M_{f_j}` on the same common refinement,

\[
\begin{aligned}
&\sum_{d_1,\ldots,d_{k-1}\mid n}
P_{d_0}M_{f_1}P_{d_1}M_{f_2}\cdots
P_{d_{k-1}}M_{f_k}P_{d_k}\\
&\qquad=
P_{d_0}M_{f_1f_2\cdots f_k}P_{d_k}.
\end{aligned}
\tag{28}
\]

Every complete unweighted sum over intermediate conductor paths therefore collapses by repeated insertion of `sum_{d|n}P_d=I`. If the endpoint sectors are also summed, one simply reconstructs multiplication by `f_1\cdots f_k`.

This matters for the live PC-215/PC-220 frontier. Merely saying “retain all conductor sectors and all paths before scalarizing” does not evade the fixed-level classicalization: **if every sector is included with equal resolution-of-identity weight, the path structure is bookkeeping rather than a new dynamical carrier.** Any surviving collective construction must select or weight sectors for a reason forced by the original geometry.

## 6. Prior-art and novelty audit

None of the abstract ingredients warrants a novelty claim.

P. P. Vaidyanathan, **Ramanujan Sums in the Context of Signal Processing—Part II: FIR Representations and Applications**, *IEEE Transactions on Signal Processing* 62:16 (2014), 4158–4172, DOI `10.1109/TSP.2014.2331624`, explicitly decomposes a period-`n` finite signal orthogonally into Ramanujan subspaces indexed by the divisors of `n`. This is a direct modern prior-art anchor for the exact-period resolution (2); PC-066 already identifies the same subspaces as the Prime-Circle exact-order projectors.

The implication

\[
\mathbb Z/n\mathbb Z\text{ local}
\iff n=p^r
\tag{29}
\]

is elementary commutative algebra/CRT. Equation (1) is therefore a project-specific realization of a textbook local-ring condition using the cyclotomic coefficient mask, not a new prime-power theorem.

The Schur/Feshbach identity in (23) is standard finite-dimensional block elimination; Crabtree--Haynsworth and the Kron-reduction references already recorded in `SOURCES.md` anchor that algebraic boundary. Likewise, the Ramanujan projector and its Fourier diagonalization are classical and already anchored repeatedly for PC-066 and PC-220.

A directed search around exact-period Ramanujan subspaces, cyclotomic coefficient Fourier transforms, finite local rings, and Schur/Feshbach block response did not locate the exact project-specific leakage criterion (1) or formula (19). That absence is **not** evidence of historical novelty. Both follow from combining the source-derived mask with standard Fourier, local-ring, and Schur-complement facts.

The strongest falsification control is immediate. Any non-arithmetic mask whose Fourier transform vanishes precisely on `U(n)` and is nonzero on every nonunit produces the same zero-leakage criterion (1), because its proof uses only the support pattern (8). Likewise, once the coefficient vector is fixed, (19) and (25) are universal compression formulas. Therefore the mechanism is not prime-specific enough to count as an RH bridge by itself.

## 7. Consequence for the research frontier

PC-220 showed that a single fixed-level transverse spectrum reduces to a signed cyclotomic-coefficient compression of the standard Ramanujan projector. PC-221 now closes the most inclusive immediate repair:

\[
\boxed{
\text{top exact-order sector}
\leftrightarrow
\text{all proper conductor sectors}
\xrightarrow{\text{unweighted collective elimination}}
\text{coefficient functional calculus + Ramanujan projection}.
}
\tag{30}
\]

The all-lower leakage does contain one clean arithmetic discriminator, but it is exactly the already-known prime-power/local-ring dichotomy and hence the support of `Lambda(n)`. Its nonzero quantitative spectrum supplies no independent phase channel, and exact Feshbach elimination supplies no hidden critical-line scale.

This does **not** rule out the entire cross-level branch. The obstruction sums every lower sector into the single complement `Q`. A source-forced construction may still survive if it resolves selected divisor sectors before summing -- for example a canonical codimension-one or divisor-depth layer -- couples several different cyclotomic masks with nontrivial intermediate projectors, or derives non-Haar matrix transport from the original root geometry. Such a continuation must explain why its sector weights/topology are forced, and it must fail a matched non-arithmetic control for a reason beyond the universal nonunit support pattern.

The practical gate is therefore sharper than PC-220's generic “go cross-level” instruction: **complete unweighted conductor assembly is exhausted. The remaining candidate must make the *selective* conductor topology itself carry source-specific information that cannot be removed by `sum P_d=I`, fixed-level Ramanujan compression, or local-ring support alone.**