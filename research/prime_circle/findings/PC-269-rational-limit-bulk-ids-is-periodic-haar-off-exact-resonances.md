# PC-269 — rational-limit bulk IDS is periodic-Haar off exact bounded resonances

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the near-resonant bulk channel left open by PC-261, PC-262 and PC-268.

Let

\[
2<p_n<r_n<q_n
\]

be distinct primes with `q_n -> infinity`, and write

\[
\alpha_n=\frac{p_n}{q_n}\to\alpha=\frac aQ,
\qquad
\beta_n=\frac{r_n}{q_n}\to\beta=\frac bQ,
\qquad
0<a<b<Q,
\tag{1}
\]

for a fixed common denominator `Q`. Unlike PC-262, the limiting torus translation is now rational and finite-order. Assume only the exact bounded-mode nonresonance condition already isolated in PC-258:

\[
\boxed{
q_n\nmid h p_n+k r_n
\quad\text{for every fixed }(h,k)\in\mathbb Z^2\setminus\{(0,0)\}
\text{ and all sufficiently large }n.
}
\tag{2}
\]

For the natively normalized shared-upper defect

\[
\Delta_n=\frac{D_{p_n,r_n;q_n}}{q_n\sqrt{p_nr_n}},
\]

let

\[
\nu_n=\frac1{p_n}\sum_{j=1}^{p_n}
\delta_{\sigma_j(\Delta_n)^2}
\tag{3}
\]

be the squared-singular-value empirical measure, including zero singular values. Then there is a deterministic probability measure

\[
\boxed{
\nu^{\mathrm{per}}_{a/Q,b/Q}
}
\tag{4}
\]

such that

\[
\boxed{
\nu_n\Longrightarrow\nu^{\mathrm{per}}_{a/Q,b/Q}.
}
\tag{5}
\]

The limit is the IDS obtained by averaging the native collision operator over Haar phase for the **finite-order translation**

\[
T_0(x,y)=\left(x+\frac aQ,y+\frac bQ\right)\pmod1,
\qquad
T_0^Q=\mathrm{id},
\tag{6}
\]

with collision window

\[
W_0=[1-a/Q,1)\times[1-b/Q,1)
\tag{7}
\]

and the same Green weight and path-incidence rules as PC-258/PC-262. Thus a rational limiting ratio does **not** by itself force the sequence-dependent resonant behavior of PC-261. The decisive distinction is whether a fixed Fourier mode is exactly annihilated at the finite prime levels.

In particular, at the PC-261 limit `(alpha,beta)=(1/4,1/2)` there are three rigorously distinct asymptotic collision branches inside the actual prime source:

\[
\boxed{
\begin{array}{c|c}
\text{finite lift} & k_n/q_n\\ \hline
2p_n+r_n=q_n & 0\\
\text{bounded-mode nonresonant} & 1/8\\
6p_n-r_n=q_n & 1/6
\end{array}}
\tag{8}
\]

where `k_n=rank D_{p_n,r_n;q_n}`. The first and third rows are PC-261; the middle row is the present theorem. Exact resonance is therefore a singular lift of the rational torus point, not the generic consequence of approaching that point.

## 1. Full raw orbit equidistribution does not require an irrational limit

Put

\[
T_n(x,y)=(x+\alpha_n,y+\beta_n)\pmod1
\]

and

\[
\mu_n=\frac1{q_n}\sum_{u=0}^{q_n-1}
\delta_{T_n^u(0,0)}.
\tag{9}
\]

PC-258 gives the exact Fourier coefficient

\[
\widehat\mu_n(h,k)
=
\frac1{q_n}\sum_{u=0}^{q_n-1}
\exp\!\left(
\frac{2\pi i u(hp_n+kr_n)}{q_n}
\right)
=
\begin{cases}
1,&q_n\mid hp_n+kr_n,\\
0,&\text{otherwise}.
\end{cases}
\tag{10}
\]

Condition (2) therefore makes every fixed nonzero Fourier coefficient eventually vanish. The Weyl criterion gives

\[
\boxed{
\mu_n\Longrightarrow m_{\mathbb T^2}
}
\tag{11}
\]

although the limiting frequency vector `(a/Q,b/Q)` is rational. Consequently the collision count still satisfies

\[
\boxed{
\frac{k_n}{q_n}\longrightarrow\alpha\beta=\frac{ab}{Q^2},
\qquad
\frac{k_n}{p_n}\longrightarrow\beta=\frac bQ.
}
\tag{12}
\]

This already separates the middle row of (8) from both exact PC-261 lifts. The subtle point is that (11) alone does not automatically control collision-index neighborhoods: near a rational limit, return times could in principle become large even while the full raw orbit is Haar-distributed. The finite-order identity (6) removes that obstruction for bulk local observables.

## 2. Finite-order recurrence replaces the irrational minimality step of PC-262

PC-262 used irrational minimality to bound the number of raw cells needed to reconstruct a fixed number of successive collision events. At the rational limit that proof is unavailable, but there is a different exact mechanism.

For any phase `x in W_0`,

\[
T_0^Qx=x.
\tag{13}
\]

Hence every collision point of the limiting system returns to the collision window within at most `Q` raw steps. More importantly, this recurrence is robust away from the finitely many boundary lines that define the mechanical words.

Fix a collision-neighborhood radius `s`. The relevant symbolic data use only finitely many translates, under powers of `T_0`, of the boundaries of

\[
[1-\alpha,1)\times\mathbb T,
\qquad
\mathbb T\times[1-\beta,1),
\qquad
W_0.
\tag{14}
\]

Because `T_0^Q=id`, only finitely many distinct boundary lines occur. Remove an `epsilon`-neighborhood of those lines. On the remaining compact good set every membership decision in one `Q`-period is separated from its threshold by a positive margin. Since `(alpha_n,beta_n)->(alpha,beta)`, for all sufficiently large `n` the complete raw symbolic word on any fixed number of consecutive `Q`-blocks is identical to the limiting word for phases in this good set.

The removed set has Haar measure `O_s(epsilon)`. Equation (11) gives the same asymptotic bound for the fraction of finite orbit points falling there. Thus, for every fixed `s`, all but `o(q_n)` collision coordinates have their radius-`s` collision neighborhood determined by a raw window of length bounded only by `sQ`, and that neighborhood converges to the one generated by the finite-order translation (6).

This is the rational analogue of the robust syndetic-return step in PC-262. It is weaker pointwise near the symbolic boundaries but equally strong after normalized bulk averaging, which is all that fixed spectral moments require.

## 3. Every fixed spectral moment has a periodic-Haar limit

Use the normalized PC-251/PC-257 collision representation

\[
M_n=R_nG_{r,n}R_nG_{p,n},
\tag{15}
\]

whose eigenvalues are the nonzero squared singular values of `Delta_n`. The matrix `M_n` has bandwidth two. Therefore, for each fixed `m>=1`,

\[
(M_n^m)_{aa}
\]

depends only on the collision weights and adjacency bits in a collision-index neighborhood of radius at most `2m`.

Section 2 turns that neighborhood, outside a set of asymptotically negligible collision coordinates, into a bounded raw-window observable of the torus phase. The exact PC-258 Green weight

\[
\rho(x,y)
=
\sqrt{\alpha\beta}\,
G\!\left(
\frac{1-x}{\alpha},
\frac{1-y}{\beta}
\right),
\qquad
G(u,v)=\min(u,v)-uv,
\tag{16}
\]

is bounded, and the adjacency bits are finite mechanical-word functions. Thus there is a bounded piecewise-continuous function `F_m^{(0)}` on `T^2`, determined by the `Q`-periodic induced collision process, such that endpoint errors and boundary-strip errors are `o(q_n)` and

\[
\frac1{p_n}\operatorname{tr}(M_n^m)
=
\frac{q_n}{p_n}
\frac1{q_n}
\sum_{u=0}^{q_n-1}
F_{m,n}(T_n^u(0,0))
+o(1),
\tag{17}
\]

with `F_{m,n}->F_m^{(0)}` away from the finite boundary arrangement. Using (11) and then shrinking the boundary strips gives

\[
\boxed{
\lim_{n\to\infty}
\int x^m\,d\nu_n(x)
=
\frac1\alpha
\int_{\mathbb T^2}F_m^{(0)}(x,y)\,dx\,dy
=:\mathcal M_m^{\mathrm{per}}(a,b;Q).
}
\tag{18}
\]

The native norm bound from PC-262 remains valid without any irrationality assumption:

\[
\|\Delta_n\|
\le\sqrt{\alpha_n\beta_n}<1.
\tag{19}
\]

Hence all `nu_n` lie in a common compact interval. The Hausdorff moment problem is determinate there, so the moments (18) define a unique measure and prove (5).

The description as a periodic-Haar IDS is literal. For Haar-almost every initial phase, the limiting raw symbolic word is `Q`-periodic; the induced collision word is therefore periodic as well. Equation (18) averages the corresponding finite-period spectral local data over Haar phase. Floquet/periodic-operator language is therefore an alternative representation of the same limit, not a new arithmetic structure.

## 4. The bounded-mode nonresonant rational regime occurs for genuine prime triples

Condition (2) is not merely an integer-control hypothesis. For every fixed target

\[
0<\alpha<\beta<1,
\]

including rational targets, there exists an all-prime sequence approaching `(alpha,beta)` and satisfying (2).

A diagonal construction uses only the prime number theorem. At stage `N`, choose a sufficiently small fixed `epsilon_N>0` and then a sufficiently large prime `q`. The intervals

\[
((\alpha-\epsilon_N)q,(\alpha+\epsilon_N)q),
\qquad
((\beta-\epsilon_N)q,(\beta+\epsilon_N)q)
\tag{20}
\]

contain arbitrarily many primes once `q` is large. Choose a prime `p` in the first interval. For the finite set

\[
0<\max(|h|,|k|)\le N,
\tag{21}
\]

each equation

\[
hp+kr=\ell q
\tag{22}
\]

with `k!=0` excludes only finitely many candidate values of `r`; the number excluded depends on `N` but not on `q`. Modes with `k=0` cannot resonate once `q>|h|`, since `p` and `q` are distinct primes. Taking `q` large enough leaves many primes in the second interval after all forbidden values are removed, so choose `r` there. Also choose `epsilon_N` smaller than one third of `beta-alpha` to preserve `p<r<q`.

Letting `epsilon_N->0` and diagonalizing in `N` gives distinct prime triples with the desired ratio limit and eventual nonresonance for every fixed mode. No prime-tuple conjecture is used. The construction deliberately proves existence rather than a quantitative counting law.

At `(alpha,beta)=(1/4,1/2)`, this supplies genuine prime sequences realizing the middle row of (8), alongside the two exact-resonance prime families already supplied by PC-261 through finite-complexity linear forms.

## 5. The rational point `(1/4,1/2)` has three different finite lifts

PC-261 proves two exact all-prime branches approaching the same rational point. The same-sign branch satisfies

\[
2p_n+r_n=q_n
\tag{23}
\]

and has

\[
D_{p_n,r_n;q_n}=0,
\qquad
k_n/q_n=0.
\tag{24}
\]

The opposite branch satisfies

\[
6p_n-r_n=q_n
\tag{25}
\]

and PC-261 gives

\[
\frac{k_n}{p_n}\to\frac23,
\qquad
\frac{k_n}{q_n}\to\frac16.
\tag{26}
\]

For the bounded-mode nonresonant branch, (12) instead gives

\[
\boxed{
\frac{k_n}{p_n}\to\frac12,
\qquad
\frac{k_n}{q_n}\to\frac18.
}
\tag{27}
\]

The generic branch is also spectrally nontrivial. Since every term in the trace expansion of (15) is nonnegative after pairing the two negative Gram off-diagonals,

\[
\operatorname{tr}M_n
\ge4\sum_{a=1}^{k_n}\rho_{n,a}^2.
\tag{28}
\]

The one-collision Haar law from PC-258 remains valid under (11), with

\[
\mathbb E(\rho^2\mid\text{collision})
=\frac{\alpha\beta}{90}.
\tag{29}
\]

Therefore

\[
\liminf_{n\to\infty}
\int x\,d\nu_n(x)
\ge
\frac{2\alpha\beta^2}{45}>0.
\tag{30}
\]

At `(1/4,1/2)` the right side is `1/360`. Hence the periodic-Haar branch cannot collapse to the zero operator of (24).

The lesson is sharper than PC-261's statement that a rational ratio pair does not determine the operator. The rational point carries a classical finite-order base dynamics, but **the finite arithmetic lift decides whether the orbit samples Haar phase or is trapped on an exact resonant subgroup**. Approximate resonance and exact resonance are discontinuously different at the bulk level.

## 6. Matched controls and RH-facing consequence

The proof of (5) uses only:

1. the exact rational-partition torus coding of PC-258;
2. absence of exact bounded Fourier annihilators;
3. the finite-order relation `T_0^Q=id`;
4. the bounded Green collision weight and path-incidence rules; and
5. compact-support moment determinacy.

None distinguishes prime labels from admissible pairwise-coprime rational-partition controls. Such controls with the same rational limiting ratios and the same bounded-mode nonresonance have the same periodic-Haar limit (4).

Therefore approaching a rational torus resonance without actually satisfying a fixed congruence relation does not create a new prime-specific bulk spectrum, critical normalization, functional equation, or zero detector. The near-resonant bulk route classicalizes to a phase-averaged periodic IDS just as the irrational route classicalizes to the induced irrational-torus IDS of PC-262.

What remains outside the theorem is genuinely finer:

- exact bounded resonances, already shown by PC-261 to have source-realizable sequence dependence;
- resonance vectors whose coefficients grow with `n` rather than remaining fixed;
- mesoscopic observation windows whose length grows on the scale at which an almost-resonant phase drifts;
- fine spacing, edge scaling, and characteristic statistics in shrinking spectral windows;
- top Lyapunov/projective data not reducible to fixed spectral moments; and
- any source-forced observable that distinguishes prime approximants from matched rational-partition controls after conditioning on the same finite lift.

Thus the surviving near-resonant question is no longer whether *rational limiting ratios* alone destroy bulk universality. They do not. A new mechanism must retain the exact finite lift, a growing-complexity resonance, or a genuinely non-bulk cocycle observable.

## 7. Prior-art and novelty audit

All abstract ingredients are classical. The Fourier criterion (10)--(11) is the standard Weyl equidistribution mechanism already used in PC-258. Finite-order torus translations and periodic symbolic codings are elementary periodic dynamics. Periodic Jacobi/finite-range spectral theory and IDS/Floquet descriptions are standard; a broad reference is Gerald Teschl, *Jacobi Operators and Completely Integrable Nonlinear Lattices*, Mathematical Surveys and Monographs 72, AMS (2000), especially the periodic and almost-periodic operator chapters. The finite-pattern/IDS literature cited in PC-262 (Lenz; Lenz--Stollmann; Lenz--Schwarzenberger--Veselic) provides the neighboring ergodic framework. The prime-existence argument in Section 4 uses only the prime number theorem in fixed proportional intervals and finite avoidance.

Targeted searches around rational-frequency approximants, periodic Jacobi IDS, periodic approximations of quasiperiodic operators, and rational rotations found the expected classical Floquet/periodic-approximation theory. Recent work such as Beckus--Bellissard--Thomas, **Spectral Regularity and Defects for the Kohmoto Model**, *Annales Henri Poincare* 27 (2026), 2117--2154, explicitly treats rational rotation parameters as periodic approximants in a neighboring Sturmian setting. None of this is evidence of novelty for the abstract mechanism.

The durable project-local content is instead the exact placement of the **PC-251/PC-257 source-forced collision operator** at the rational-limit boundary omitted by PC-262: full raw Haar equidistribution plus finite-order recurrence is enough to recover deterministic bulk spectral convergence even when the limiting frequency is rational, while the exact congruence lifts of PC-261 remain singular exceptions. The three-branch comparison (8) makes the boundary explicit inside genuine prime triples.

No novelty is claimed for Weyl equidistribution, periodic IDS, Floquet theory, rational rotations, or the prime number theorem.

## 8. Falsification and boundary audit

The theorem has direct failure tests.

1. **Raw Haar step:** find a fixed nonzero `(h,k)` for which (2) holds but the exact Fourier coefficient (10) does not vanish eventually.
2. **Finite-order recurrence:** produce a phase a positive distance from the limiting symbolic boundaries whose fixed collision neighborhood is not stable under sufficiently close `(alpha_n,beta_n)` despite `T_0^Q=id`.
3. **Boundary control:** produce a fixed moment for which the required unstable-phase set has positive Haar measure rather than being contained in finitely many translated boundary lines.
4. **Moment locality:** violate PC-257 by making `(M_n^m)_{aa}` depend on collision coordinates farther than `2m` away for fixed `m`.
5. **Compactness:** violate the native norm bound (19).
6. **Prime realizability:** show that finitely many resonance equations can exhaust all primes in one of the fixed proportional intervals in (20), contrary to the prime number theorem.
7. **Matched control:** preserve the same torus coding, Green rule, rational target and bounded-mode nonresonance but obtain a different fixed-moment limit.

The result is intentionally a **bulk fixed-moment/IDS theorem**. It makes no claim of uniformity as the resonance complexity grows, no microscopic spacing theorem, and no Lyapunov no-go. Those exclusions are essential: they are exactly where PC-268 leaves the long-cocycle frontier open.