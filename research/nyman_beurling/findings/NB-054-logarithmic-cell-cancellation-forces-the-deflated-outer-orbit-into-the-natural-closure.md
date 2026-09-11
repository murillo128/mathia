# NB-054 — logarithmic cell cancellation forces the deflated outer orbit into the natural closure

**Status:** `EXACT-DERIVED + DEBLASCHKE-ORBIT-IDENTITY + VECTOR-CELL-CANCELLATION + UNIFORM-OUTER-ORBIT-QUOTIENT-COLLAPSE + FINITE-GRID-TAIL-ENVELOPE + NEGATIVE/METHOD-BOUNDARY + LITERATURE-BOUNDED`.

`NB-052` identifies the limiting weighted-repair gap with the deflated natural target defect

\[
\Delta_*=B(1)^2\delta_{\rm def}^2,
\qquad
\delta_{\rm def}
=
\operatorname{dist}(k_1,\mathcal A_{\rm nat}),
\qquad
k_1(s)=\frac1s,
\tag{1}
\]

inside

\[
\mathcal H^2:=H^2(\Re s>1/2),
\qquad
\mathcal A_{\rm nat}
=
\overline{\operatorname{span}}
\{\phi_{1/n}:n\ge2\}.
\tag{2}
\]

`NB-053` then shows that the remaining defect is purely off the logarithmic integer grid: `A_nat` is invariant under `U_(log n)`, two natural generators have full continuous-shift hull, and a fixed vector in `A_nat^perp` has vanishing large-shift co-invariance leakage only **vectorwise**. It explicitly leaves open the absence of an operator-norm regularity statement for moving defects.

The present result finds a different uniform statement which is available because the continuous Nyman generators are not arbitrary shifts: after Burnol deflation they are **integrals of one fixed outer orbit**. Let

\[
O(s)=\frac{s-1}{s}\frac{\zeta(s)}{B(s)}
\tag{3}
\]

be Burnol's outer factor, let

\[
(U_tF)(s)=e^{-t(s-1/2)}F(s),
\qquad t\ge0,
\tag{4}
\]

and write

\[
P=P_{\mathcal A_{\rm nat}},
\qquad
Q=I-P.
\tag{5}
\]

Then the reciprocal-integer orthogonality is equivalent to an exact **vector-valued zero-mean law on every logarithmic cell**:

\[
\boxed{
\int_{\log n}^{\log(n+1)}
 e^{u/2}\,Q U_uO\,du=0
\qquad(n\ge1).
}
\tag{6}
\]

Because the cells shrink and the orbit of the single fixed vector `O` is norm-continuous, (6) has a consequence stronger than the fixed-witness statement in `NB-053`. If

\[
\omega_O(r)
:=
\sup_{0\le v\le r}
\|U_vO-O\|,
\tag{7}
\]

then `omega_O(r)->0` as `r->0`, and

\[
\boxed{
\sup_{t\ge\log N}
\operatorname{dist}(U_tO,\mathcal A_{\rm nat})
\le
\omega_O\!\left(\log\left(1+\frac1N\right)\right)
\longrightarrow0.
}
\tag{8}
\]

Thus the fixed-norm outer orbit itself is asymptotically swallowed by the natural deflated closure. This is **not** the false operator-norm assertion `||Q U_t||->0`: only the distinguished source orbit `U_tO` is controlled. By duality, however, (8) is uniform over *all* unit defect witnesses `h in A_nat^perp` when they are tested against that orbit.

The same cancellation gives a quantitative envelope for every continuous generator between two adjacent natural parameters. For

\[
a\in[\log n,\log(n+1)],
\qquad
\theta=e^{-a},
\qquad
\Delta_n=\log\left(1+\frac1n\right),
\tag{9}
\]

one has

\[
\boxed{
\operatorname{dist}(\phi_\theta,\mathcal A_{\rm nat})
\le
2e^{-a}\omega_O(\Delta_n)
\min\!\left(
 e^{a/2}-\sqrt n,
 \sqrt{n+1}-e^{a/2}
\right),
}
\tag{10}
\]

and therefore

\[
\boxed{
\sup_{1/(n+1)\le\theta\le1/n}
\operatorname{dist}(\phi_\theta,\mathcal A_{\rm nat})
\le
\frac{\omega_O(\Delta_n)}{2n^{3/2}}
=o(n^{-3/2}).
}
\tag{11}
\]

For the `NB-050` finite grid `theta=M/k`, this says that the **raw quotient columns at large ratio are uniformly negligible**. More precisely, for every integer `R>=1`, uniformly in `M` and in every truncation `N`,

\[
\boxed{
\frac1M
\sum_{\substack{M<k\le N\\ k/M\ge R}}
\|Q\phi_{M/k}\|^2
\le
\frac14
\sum_{j\ge R}
\frac{\omega_O(\Delta_j)^2}{j^3}
=
o(R^{-2}).
}
\tag{12}
\]

This does **not** make the repair gap small. A span is unchanged when a nonzero column is rescaled, so a collection of tiny quotient vectors can still carry substantial target geometry after normalization or Gram whitening. Equation (12) instead rules out a simpler route: the `NB-050`--`NB-052` enrichment cannot be explained by persistent large-ratio raw column mass. Any such information must survive through the directions/conditioning of increasingly small quotient columns, or be supplied at bounded and moderate ratios.

## 1. The continuous generator is an integrated outer orbit

`NB-053` uses

\[
\phi_\theta(s)
=
O(s)\frac{\theta-\theta^s}{s-1}.
\tag{13}
\]

Put `theta=e^{-a}`. Then

\[
\begin{aligned}
\phi_{e^{-a}}(s)
&=
e^{-a}O(s)
\frac{1-e^{-a(s-1)}}{s-1}\\
&=
e^{-a}\int_0^a
 e^{-u(s-1)}O(s)\,du\\
&=
e^{-a}\int_0^a
 e^{u/2}U_uO(s)\,du.
\end{aligned}
\tag{14}
\]

The integral is a Bochner integral in `H^2`: `u -> U_uO` is strongly continuous and `U_u` is an isometry. Hence the identity is an equality in the Hilbert space, not merely a pointwise formula.

It is useful to remove the scalar prefactor and project to the natural quotient. Define

\[
G(a)
:=
e^aQ\phi_{e^{-a}}
=
\int_0^a e^{u/2}Q U_uO\,du.
\tag{15}
\]

For every integer `n>=2`, `phi_(1/n)` belongs to `A_nat`; also `phi_1=0`. Therefore

\[
\boxed{
G(\log n)=0
\qquad(n\ge1).
}
\tag{16}
\]

Subtracting two consecutive identities in (16) gives exactly (6).

There is also an equivalent scalar sampling form. For any `h in H^2`, with the inner product convention linear in the first entry, set

\[
F_h(a)
:=
e^a\langle h,\phi_{e^{-a}}\rangle
=
\int_0^a e^{u/2}\langle h,U_uO\rangle\,du.
\tag{17}
\]

Then

\[
\boxed{
h\in\mathcal A_{\rm nat}^{\perp}
\iff
F_h(\log n)=0
\quad\text{for every }n\ge2.
}
\tag{18}
\]

Thus the natural orthogonal defect is the kernel of the **discrete samples of an injective continuous orbit primitive**. The continuous family is complete after deflation by Burnol, so `F_h(a)=0` for every `a>=0` forces `h=0`; a nonzero defect can survive only because the primitive is sampled at the special set `log N`.

For `h in A_nat^perp`, (17)--(18) give the exact scalar cell law

\[
\int_{\log n}^{\log(n+1)}
 e^{u/2}\langle h,U_uO\rangle\,du=0.
\tag{19}
\]

Equation (6) is strictly stronger bookkeeping: it records all such scalar cancellations simultaneously as one quotient-space identity.

## 2. Shrinking cells force the fixed outer orbit into the natural closure

Let

\[
I_n=[\log n,\log(n+1)],
\qquad
\Delta_n=|I_n|=\log(1+1/n).
\tag{20}
\]

Fix `t in I_n` and define

\[
W_n:=\int_{I_n}e^{u/2}\,du>0.
\tag{21}
\]

Using (6),

\[
\begin{aligned}
Q U_tO
&=
\frac1{W_n}
\int_{I_n}e^{u/2}
Q(U_tO-U_uO)\,du.
\end{aligned}
\tag{22}
\]

For `t,u in I_n`, the semigroup isometry gives

\[
\|U_tO-U_uO\|
\le
\omega_O(\Delta_n).
\tag{23}
\]

Indeed, if `t>=u`,

\[
U_tO-U_uO
=
U_u(U_{t-u}O-O),
\tag{24}
\]

and the opposite ordering is symmetric. Since `Q` is a contraction, (22)--(23) yield

\[
\boxed{
\sup_{t\in I_n}
\|Q U_tO\|
\le
\omega_O(\Delta_n).
}
\tag{25}
\]

Strong continuity for the **fixed vector** `O` implies

\[
\omega_O(r)\to0
\qquad(r\downarrow0),
\tag{26}
\]

while `Delta_n->0`. Because the cell widths decrease with `n`, (25) immediately gives (8).

This is the main qualitative strengthening over `NB-053`. There the map

\[
h\mapsto P U_t^*h,
\qquad h\in\mathcal A_{\rm nat}^{\perp},
\tag{27}
\]

was controlled only for each fixed `h`; norm continuity of the entire shift semigroup is unavailable. Here no operator-norm continuity is invoked. The vector `O` is fixed, its orbit is norm-continuous, and the exact Nyman endpoint cancellations turn that fixed-vector continuity into the uniform quotient statement (8).

Equivalently, for every unit `h in A_nat^perp`,

\[
\boxed{
\sup_{t\ge\log N}
|\langle h,U_tO\rangle|
\le
\omega_O\!\left(\log(1+1/N)\right).
}
\tag{28}
\]

The modulus on the right is source-side: it depends only on the single Burnol outer factor, not on the particular defect witness.

## 3. Adjacent natural parameters give a sharp quotient bridge

Equation (15) and the left endpoint `G(log n)=0` give, for `a in I_n`,

\[
Q\phi_{e^{-a}}
=
e^{-a}
\int_{\log n}^{a}
 e^{u/2}Q U_uO\,du.
\tag{29}
\]

The right endpoint is also zero, so (6) equivalently gives

\[
Q\phi_{e^{-a}}
=
-e^{-a}
\int_{a}^{\log(n+1)}
 e^{u/2}Q U_uO\,du.
\tag{30}
\]

Applying (25) to the shorter of these two integrals yields (10), because

\[
\int_{\log n}^{a}e^{u/2}du
=2(e^{a/2}-\sqrt n)
\tag{31}
\]

and

\[
\int_a^{\log(n+1)}e^{u/2}du
=2(\sqrt{n+1}-e^{a/2}).
\tag{32}
\]

Since

\[
2\min(x,y)\le x+y,
\qquad
\sqrt{n+1}-\sqrt n
=\frac1{\sqrt{n+1}+\sqrt n},
\tag{33}
\]

and `e^{-a}<=1/n`, (10) gives

\[
\|Q\phi_{e^{-a}}\|
\le
\frac{\omega_O(\Delta_n)}
{n(\sqrt{n+1}+\sqrt n)}
\le
\frac{\omega_O(\Delta_n)}{2n^{3/2}},
\tag{34}
\]

which is (11).

The infinitesimal version identifies the missing quotient direction near each natural point. Differentiating (14) in `H^2` gives

\[
\frac d{da}\phi_{e^{-a}}
=
-\phi_{e^{-a}}+e^{-a/2}U_aO.
\tag{35}
\]

At `a=log n`, the first term lies in `A_nat`, so

\[
\boxed{
Q\frac d{da}\phi_{e^{-a}}\bigg|_{a=\log n}
=
n^{-1/2}Q U_{\log n}O.
}
\tag{36}
\]

Combining (25) with (36),

\[
\boxed{
\left\|
Q\frac d{da}\phi_{e^{-a}}\bigg|_{a=\log n}
\right\|
\le
n^{-1/2}\omega_O(\Delta_n)
=o(n^{-1/2}).
}
\tag{37}
\]

So even the **normalized tangent mechanism** by which the continuous parameter leaves the natural grid becomes asymptotically redundant in the natural quotient at large integer ratios. This does not say the quotient directions stabilize after normalization by their own tiny norms; only their absolute quotient size is controlled.

## 4. The NB-050 finite grid samples exactly these zero-endpoint bridges

The deflated finite enrichment space in `NB-052` is

\[
\mathcal D_{M,N}
=
\operatorname{span}
\{\phi_{M/k}:M<k\le N\}.
\tag{38}
\]

Writing

\[
a_{M,k}=\log\frac{k}{M},
\tag{39}
\]

(17) gives the exact target-witness sample

\[
\boxed{
\langle h,\phi_{M/k}\rangle
=
\frac{M}{k}
F_h\!\left(\log\frac{k}{M}\right)
\qquad(h\in\mathcal A_{\rm nat}^{\perp}).
}
\tag{40}
\]

If `k/M` is an integer, the sample vanishes exactly. Otherwise it lies inside the bridge whose endpoints are the two adjacent integer ratios. Thus the `NB-050` grid does not merely use unspecified off-grid geometry: it samples a family of continuous bridges with **exact zero boundary values at every integer ratio**.

Let

\[
j=\left\lfloor\frac{k}{M}\right\rfloor.
\tag{41}
\]

When `k/M` is not an integer, (11) gives

\[
\boxed{
\|Q\phi_{M/k}\|
\le
\frac{\omega_O(\Delta_j)}{2j^{3/2}}.
}
\tag{42}
\]

At integer ratios the left side is exactly zero. There are at most `M` noninteger sample points in each ratio cell `[j,j+1]`. Consequently, for integer `R>=1`,

\[
\begin{aligned}
\frac1M
\sum_{\substack{M<k\le N\\ k/M\ge R}}
\|Q\phi_{M/k}\|^2
&\le
\frac14
\sum_{j\ge R}
\frac{\omega_O(\Delta_j)^2}{j^3}.
\end{aligned}
\tag{43}
\]

Because `omega_O(Delta_j)->0` and

\[
\sum_{j\ge R}j^{-3}=O(R^{-2}),
\tag{44}
\]

the right side is `o(R^-2)`, proving (12), uniformly in both finite-grid parameters.

This gives a useful separation. The raw quotient-vector energy of the continuous grid is **uniformly front-loaded in bounded ratio**. Yet `NB-051` says that allowing the ratio horizon `N/M` to diverge ultimately recovers the full continuous closure. The two statements are consistent only because closure is sensitive to directions after arbitrary rescaling, not to the raw Hilbert--Schmidt size of the columns. Large-ratio cells can remain geometrically necessary while carrying vanishing unnormalized energy.

That is exactly the kind of phenomenon already encountered earlier in the weighted-skeleton line: target preservation is a conditioned/whitened question, not a raw-Gram or raw-column-size question.

## 5. Matched control: the collapse is semigroup geometry, not new arithmetic rigidity

The implication from cell cancellation to (8) is not specific to zeta once the representation (14) is available. Let `U_t` be any strongly continuous isometric semigroup on a Hilbert space, fix a vector `O`, and define

\[
v(a)=e^{-a}\int_0^a e^{u/2}U_uO\,du.
\tag{45}
\]

If a closed subspace `A` contains `v(log n)` for every positive integer `n`, then its quotient projection `Q` satisfies exactly the same cell cancellation (6), hence

\[
\sup_{t\ge\log N}\|Q U_tO\|
\le
\omega_O(\log(1+1/N))
\to0.
\tag{46}
\]

Thus (8) should **not** be read as hidden RH rigidity. The arithmetic/Nyman input is the identification of the actual deflated generators with the integrated orbit (14), together with the reciprocal-integer sampling that defines `A_nat`. Once those facts are in place, the asymptotic quotient collapse is universal semigroup geometry.

This matched control is important for interpretation. It prevents using (8) as if it supplied a new zero-free region or approximation rate. Its value is instead to remove a class of possible mechanisms for the already-isolated repair defect: persistent large-shift raw coupling of the distinguished outer orbit is impossible even when `A_nat` is a proper subspace.

## 6. Prior-art boundary

The load-bearing ingredients are classical and already anchored in `SOURCES.md`. Burnol supplies the continuous Nyman closure, the Blaschke/outer factorization, and the deflated generator setting used by `NB-052`. Bagchi and the classical Nyman/Báez-Duarte formulation supply the multiplicative semigroup viewpoint. None of those ingredients is claimed new here.

A targeted audit also checked Francisco Calderaro, Juan Manzur, Waleed Noor and Charles Santos, *Orthogonality questions in the Hardy space related to zeta-zeros*, arXiv:2203.05030v4. That work studies the Hardy-space orthogonal complement of the natural Báez-Duarte family, excludes substantial regularity classes from it, and treats shift-invariance of the natural closure as an RH-sensitive question. Accordingly, neither the generic study of `A_nat^perp` nor the idea that shift geometry constrains that orthogonal complement is a novelty claim of this finding.

The line-local delta is narrower: after the exact Blaschke deflation of `NB-052` and the off-grid reduction of `NB-053`, equations (6), (8), and (12) identify the remaining natural-vs-continuous defect with a **zero-endpoint logarithmic-cell bridge system** and prove a uniform asymptotic quotient collapse for the distinguished outer orbit. No located source in the audit stated this vector cell cancellation or its finite-grid raw-tail consequence in the `NB-050`--`NB-053` repair coordinates. Since no new external theorem is load-bearing, `SOURCES.md` is unchanged.

## 7. Failure modes and consequence for the live bridge

The result deliberately stops short of three stronger conclusions.

First, (8) is not

\[
\|Q U_t\|\to0
\quad\text{or}\quad
\|P U_t^*Q\|\to0.
\tag{47}
\]

The shift semigroup is not norm-continuous at zero, and `NB-053` correctly keeps the full leakage operator outside its vectorwise conclusion. `NB-054` controls only the orbit of the fixed source vector `O` (and therefore its scalar pairing uniformly over unit defect witnesses).

Second, (11)--(12) do not bound the target improvement obtained by adjoining the corresponding quotient directions. If

\[
q=Q\phi_\theta
\tag{48}
\]

is tiny but nonzero, `span(q)` is unchanged after dividing by `||q||`. Without a lower frame bound, principal-angle estimate, coefficient bound, or quotient-Gram control, raw smallness of `q` does not imply a small projection gain. Any argument making that inference would repeat the Gram-versus-target mistake already ruled out repeatedly in this research line.

Third, the canonical **finite-section** residuals do not lie in `A_nat^perp`; they are orthogonal only to their own finite section. Hence (28) does not automatically provide the source-uniform regularity modulus for moving finite residuals requested at the end of `NB-053`. Transferring the cell mechanism to those moving residuals would require a quantitative finite-section defect term, and inserting `d_N` or the full projector as that term would be circular.

The surviving bridge is therefore sharper. The closure-level defect cannot live in another inner factor (`NB-052`), cannot rely on persistent large-shift leakage of a fixed witness (`NB-053`), and now cannot rely on persistent large-shift **raw outer-orbit or raw quotient-column mass** either. What can still carry the repair information is:

- bounded/moderate logarithmic cells, where the bridge amplitudes need not be small;
- normalized directions of tiny high-ratio quotient columns and their Gram conditioning;
- or a finite-section correction that breaks the exact zero-cell law by a quantitatively source-controlled amount.

No estimate of `delta_def`, `Delta_*`, or `d_N` is obtained, and no RH implication follows. The contribution is an exact normal form plus a method boundary: after deflation, the natural-vs-continuous repair defect is a logarithmic-cell sampling/conditioning problem rather than a persistent large-scale amplitude problem.