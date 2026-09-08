# ANF-129 — critical exponential digit density evacuates the saddle without source blowup

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CRITICAL-EXPONENTIAL-BUDGET + BOUNDED-MACROSCOPIC-SOURCE + SAME-SADDLE-DIGIT-CLOUD + SUPEREXPONENTIAL-SADDLE-EVACUATION + FIXED-NOTCH-DARK + GLOBAL-COMPLETION-GATE`. `ANF-126` shows that a successful same-chamber mirror is globally excisable when its unsigned source budget is subexponential in `A`. `ANF-127` proves that every positive exponential budget scale can escape that theorem by coherently resurrecting a remote tail, but its displayed construction deliberately chooses the digit density so that the new reservoir is exponentially oversized. `ANF-128` shows that an exponential layer can also evade a polynomial-depth arithmetic ladder while regenerating the same oversized source.

The oversize is **not forced**. For every fixed `ANF-115` packet family there is a sequence of fixed `q`-ary digit architectures with positive exponential unsigned-budget rates `rho_q -> 0` such that, after tuning the repetition density to a critical value, the complete translated cloud has source energy comparable to one base packet, while every shrinking macroscopic chamber around the original saddle is superexponentially evacuated. The regenerated source sits only `Theta(q^{-2})` away from the cancelled saddle, remains outside every fixed central notch for large fixed `q`, and the cloud's affine cardinality is exponentially negligible on the natural ambient scale `L_A ~ E_A`.

More precisely, if `a=a_gamma`, `c_gamma=-F_gamma''(a)>0`,

\[
D_q(x):=\sum_{v=0}^{q-1}e^{-2\pi i v x},
\qquad
d_q:=\frac{q-1}{qa},
\]

and

\[
K_q
:=d_q\left|D_q'\!\left(\frac{q-1}{q}\right)\right|
=d_q\frac{\pi q}{\sin(\pi/q)},
\tag{1}
\]

then there are critical repetition densities `r_q>0` satisfying

\[
\boxed{
r_qK_q^2\longrightarrow\frac{e\,c_\gamma}{2}
\qquad(q\to\infty),
}
\tag{2}
\]

and therefore critical unsigned-budget rates

\[
\boxed{
\rho_q:=r_q\log q
\sim
\frac{e\,c_\gamma a^2}{2}\,
\frac{\log q}{q^4}
\longrightarrow0.
}
\tag{3}
\]

For each sufficiently large **fixed** `q`, taking `h_A=floor(r_qA)` digit levels produces a distinct positive physical cloud `T_A` with

\[
\frac1A\log\mathcal U_A\to\rho_q>0,
\qquad
0<c_q\le\frac{E_0(T_A)}{E_A}\le C_q<\infty,
\tag{4}
\]

while its original saddle chamber has source ratio `exp(-omega(A))` on the exponential scale. Thus the remaining exponential branch already contains a genuinely non-excisable **bounded-macroscopic-source** block. A second cancellation layer is not needed merely to prevent source blowup; it is needed only if global near-extremizer bookkeeping forces further anti-alignment.

## 1. The repeated digit has a one-parameter source landscape

Fix `gamma>0` and let

\[
P_A:=P_{A,\lfloor\gamma A\rfloor}
\]

be the `ANF-115` packet. Write

\[
E_A:=E_0(P_A),
\qquad
m_A:=|P_A|,
\qquad
a:=a_\gamma,
\qquad
f:=F_\gamma(a),
\]

where

\[
F_\gamma(\alpha)
=\alpha+2\gamma\log\cos\frac{\pi\alpha}{2},
\qquad
F_\gamma'(a)=0,
\qquad
c_\gamma:=-F_\gamma''(a)>0.
\tag{5}
\]

`ANF-115` gives

\[
\frac1A\log\frac{E_A}{m_A^2}\to f,
\tag{6}
\]

and the exact packet formula gives the usual nondegenerate Gaussian Laplace profile at `+-a`.

Fix an integer `q` sufficiently large that

\[
\beta_q:=\frac{qa}{q-1}<1,
\qquad
d_q=\beta_q^{-1}.
\tag{7}
\]

Then

\[
ad_q=1-\frac1q,
\qquad
D_q(ad_q)=0.
\tag{8}
\]

For an ideal repetition density `r>0`, define on `0<=alpha<1`

\[
\boxed{
\Psi_{q,r}(\alpha)
:=F_\gamma(\alpha)-f
+2r\log|D_q(d_q\alpha)|,
}
\tag{9}
\]

with value `-infinity` at a zero of `D_q`, and put

\[
M_q(r):=\sup_{0\le\alpha<1}\Psi_{q,r}(\alpha).
\tag{10}
\]

If `h_A=rA+O(1)` identical digit factors were used, `M_q(r)` would be exactly the additional exponential rate of the cloud source norm relative to `E_A`. The distinctness perturbations used below change this rate by `o(1)` and do not affect the critical calculation.

The crucial feature is that the original saddle is a **simple zero** of the digit factor. Let `delta=alpha-a`. From the geometric-sum formula,

\[
\left|D_q'\!\left(1-\frac1q\right)\right|
=\frac{\pi q}{\sin(\pi/q)},
\]

so with `K_q` from (1),

\[
D_q(d_q(a+\delta))
=e^{i\vartheta_q}K_q\delta
+O_q(\delta^2)
\tag{11}
\]

for a harmless phase `vartheta_q`. At the same time,

\[
F_\gamma(a+\delta)-f
=-\frac{c_\gamma}{2}\delta^2+O_\gamma(\delta^3).
\tag{12}
\]

Thus repeating the zero has two competing effects: the base packet pays a quadratic saddle penalty when the source moves away from `a`, while the digit product gains logarithmically with the displacement from its root.

## 2. A critical repetition density exists and is `Theta(q^{-4})`

The balance can be resolved sharply. For fixed `lambda>0`, set

\[
r=\frac{\lambda}{K_q^2},
\qquad
\alpha=a+\frac{u}{K_q}.
\tag{13}
\]

Since `K_q~q^2/a`, equations (11)--(12) give locally uniformly for fixed nonzero `u`,

\[
K_q^2\Psi_{q,\lambda/K_q^2}
\left(a+\frac{u}{K_q}\right)
\longrightarrow
-\frac{c_\gamma}{2}u^2
+2\lambda\log|u|.
\tag{14}
\]

The right side has its maxima at

\[
u^2=\frac{2\lambda}{c_\gamma}
\]

and maximal value

\[
\boxed{
\lambda\left(
\log\frac{2\lambda}{c_\gamma}-1
\right).
}
\tag{15}
\]

This local scaling controls the global maximum. Indeed, away from a fixed neighborhood of `a`, strict maximality of `F_gamma` gives a fixed negative gap while the digit gain is only `O(K_q^{-2}\log q)`. Inside that neighborhood, the bound `|D_q|<=q` and strict concavity of `F_gamma` first confine any maximizer to

\[
|\alpha-a|
\ll\frac{\sqrt{\log q}}{K_q},
\]

where (11) is uniform after the rescaling (13). Consequently, locally uniformly for `lambda` in compact subsets of `(0,infinity)`,

\[
\boxed{
K_q^2M_q\!\left(\frac{\lambda}{K_q^2}\right)
\longrightarrow
\lambda\left(
\log\frac{2\lambda}{c_\gamma}-1
\right).
}
\tag{16}
\]

The limiting expression is negative for

\[
0<\lambda<\frac{e c_\gamma}{2}
\]

and positive for

\[
\lambda>\frac{e c_\gamma}{2}.
\]

For each large `q`, `M_q(r)` is continuous for positive `r` because it is the supremum on a compact interval of the continuous finite branches between the finitely many digit zeros, with the zeros tending to `-infinity`. Equation (16) therefore gives a critical value `r_q` with

\[
M_q(r_q)=0
\tag{17}
\]

and the asymptotic (2). Since

\[
K_q
=d_q\frac{\pi q}{\sin(\pi/q)}
=\frac{q^2}{a}(1+o(1)),
\tag{18}
\]

(3) follows.

The same scaling locates the regenerated source. Any critical maximizing branch participating in (17) satisfies

\[
\boxed{
K_q|\alpha_q-a|\longrightarrow\sqrt e
\qquad(q\to\infty).
}
\tag{19}
\]

Thus the critical cloud does not need to travel all the way to the fully coherent point `beta_q-a=Theta(q^{-1})` used in `ANF-127`. It balances already in the immediate leakage zone of the cancelled root, at distance

\[
|\alpha_q-a|=\Theta(q^{-2}).
\tag{20}
\]

This is why the required exponential budget rate is `Theta((log q)/q^4)`, parametrically smaller than the `Theta(q^{-2})` large-deviation scale of the coherent endpoint in `ANF-127`.

## 3. Criticality gives source mass comparable to one packet, not merely the same exponential rate

To pass from the ideal landscape to a physical cloud, let

\[
h_A:=\lfloor r_qA\rfloor.
\tag{21}
\]

Choose positive spacings

\[
d_{\ell,A}=d_q+O(A^{-4}),
\qquad 1\le\ell\le h_A,
\tag{22}
\]

so that every physical point generated below is distinct. Exactly as in `ANF-127`, this is possible inductively because at every finite stage each unwanted collision excludes only finitely many choices for the next spacing inside an arbitrarily small interval around `d_q`.

For digits `v_ell in {0,...,q-1}`, set

\[
\tau_v:=\sum_{\ell=1}^{h_A}v_\ell d_{\ell,A}
\]

and form

\[
T_A
:=
\bigsqcup_{v\in\{0,\ldots,q-1\}^{h_A}}
(P_A+\tau_v).
\tag{23}
\]

There are

\[
R_A=q^{h_A}
\]

translated copies and, because every constituent is the same packet,

\[
\mathcal U_A=R_A,
\qquad
\boxed{
\frac1A\log\mathcal U_A
\to r_q\log q=\rho_q>0.
}
\tag{24}
\]

Translation again gives the exact physical factorization

\[
S_{T_A}(\alpha)
=p_A(\alpha)S_{P_A}(\alpha),
\qquad
p_A(\alpha)
=
\prod_{\ell=1}^{h_A}
D_q(\alpha d_{\ell,A}).
\tag{25}
\]

For fixed `q`, every critical maximizer of `Psi_{q,r_q}` stays a positive fixed distance from the digit zeros. On a neighborhood of that finite critical set, (22) changes `log|p_A|` from

\[
h_A\log|D_q(d_q\alpha)|
\]

by `o(1)`. The `ANF-115` distinctness perturbation likewise changes the base exponent by only `o(1)` there.

The critical maxima are nondegenerate. On each interval between zeros of `D_q`, the geometric-sum identity gives

\[
\frac{d^2}{dx^2}\log|D_q(x)|
=
\pi^2\csc^2(\pi x)
-
\pi^2q^2\csc^2(\pi qx)
\le0,
\tag{26}
\]

where the inequality is the elementary multiple-angle bound

\[
|\sin(qt)|\le q|\sin t|.
\]

Since `F_gamma''<0`, every branch of `Psi_{q,r_q}` is strictly concave. Hence the global critical set is finite and consists of nondegenerate interior maxima. Applying the elementary Gaussian Laplace comparison to the exact packet density in the denominator and to the finitely many critical maxima in the numerator yields constants depending on the fixed `q` and `gamma` but not on `A` such that

\[
\boxed{
0<c_q
\le
\frac{E_0(T_A)}{E_A}
\le
C_q<\infty.
}
\tag{27}
\]

The floor in (21) can prevent a literal limit because it leaves a bounded multiplicative factor `|D_q|^{-2{r_qA}}` at the maximizing chamber. This is why (27), rather than an unnecessary convergence claim, is the stable statement.

Thus the critical tuning does more than arrange zero exponential growth: it produces a source-heavy block of exactly the macroscopic order relevant to a global normalization `L_A asymp E_A`.

## 4. The original saddle is still superexponentially evacuated

Let `S_A>0` satisfy

\[
\frac{S_A}{\sqrt A}\to0
\]

and define

\[
B_A(S_A)
:=
\left\{
\alpha\in[-1,1]:
\bigl||\alpha|-a\bigr|
\le\frac{S_A}{\sqrt A}
\right\}.
\tag{28}
\]

The digit zero at `ad_q=1-1/q` is simple. Equations (22) and (25) therefore give, uniformly on this chamber,

\[
|D_q(\alpha d_{\ell,A})|
\le
C_q\left(
\frac{S_A}{\sqrt A}+A^{-4}
\right).
\tag{29}
\]

Since `h_A/A->r_q>0`,

\[
\boxed{
\frac1A\log
\sup_{\alpha\in B_A(S_A)}|p_A(\alpha)|^2
\to-\infty.
}
\tag{30}
\]

Consequently

\[
\boxed{
\frac1A\log
\frac{E_{B_A(S_A)}(T_A)}{E_A}
\to-\infty.
}
\tag{31}
\]

The complete natural saddle chamber can therefore be cancelled much more strongly than the local-mirror hypothesis of `ANF-126`, while (27) proves that the aggregate as a whole is **not** source-negligible. The missing source has simply reappeared in the nearby critical chambers from (19).

This also explains why there is no contradiction with `ANF-126`. For every fixed `q`, `rho_q` is positive, so

\[
\log\mathcal U_A\sim\rho_qA
\]

violates its subexponential-budget hypothesis, however tiny `rho_q` is. The limit `rho_q->0` is taken only after the `A->infinity` construction for each fixed `q`. A diagonal choice `q=q(A)->infinity` is a different regime: its regenerated chamber approaches the original saddle and must be compared with the widening mesoscopic band of `ANF-126`; no diagonal escape is claimed here.

## 5. The bounded-source block remains fixed-notch dark and affine-negligible

Fix a central notch width

\[
0<\eta<a.
\]

The base packet has the strict large-deviation gap

\[
\Delta_\eta
:=
f-
\sup_{0\le\alpha\le\eta}F_\gamma(\alpha)
>0.
\tag{32}
\]

Since `|D_q|<=q`, equations (24)--(25) give

\[
\frac{E_\eta(T_A)}{E_A}
\le
\exp\left(
-(\Delta_\eta-2\rho_q+o(1))A
\right).
\tag{33}
\]

By (3), choose `q` so large that

\[
2\rho_q<\Delta_\eta.
\tag{34}
\]

Then

\[
\boxed{
\frac{E_\eta(T_A)}{E_A}\to0
\quad\text{exponentially}.
}
\tag{35}
\]

The same large-`q` choice makes the cloud negligible in the affine denominator on the natural base-packet source scale. From `ANF-115`,

\[
\frac1A\log m_A=\gamma\log2+o(1),
\qquad
\frac1A\log E_A
=2\gamma\log2+f+o(1).
\tag{36}
\]

Since `|T_A|=R_Am_A`,

\[
\frac1A\log\frac{|T_A|}{E_A}
=
\rho_q-\gamma\log2-f+o(1).
\tag{37}
\]

Because `rho_q->0` while `gamma log2+f>0`, for all sufficiently large fixed `q`,

\[
\boxed{
|T_A|=o(E_A)
\quad\text{exponentially}.
}
\tag{38}
\]

Thus if the ambient normalization is chosen at the source-heavy scale

\[
L_A\asymp E_A,
\]

then `T_A` changes the affine denominator by only `o(L_A)` while carrying `Theta(L_A)` source energy and `o(L_A)` fixed-notch energy. This is exactly the combination that prevents source excision but still demands macroscopic anti-alignment from the rest of any global near-extremizer.

There is no conflict with `ANF-100`: the cloud `T_A` **by itself** is extremely far from Montgomery--Taylor near-extremal when normalized by its own cardinality. The statement here concerns its role as an affine-negligible, source-macroscopic block inside a much larger normalization, which is the regime isolated by `ANF-097` and the later packet-completion analysis.

## 6. What this changes in the exponential cascade gate

`ANF-127` correctly proves that for every prescribed positive rate `rho` one can choose a digit architecture whose coherent endpoint is exponentially oversized, and `ANF-128` correctly shows that this reservoir can be hidden from a polynomial-depth arithmetic ladder. Those constructions establish scale sharpness and checkpoint insufficiency. The present critical tuning answers a different question: **is exponential source blowup an unavoidable intermediate state once the original saddle has been cancelled?** The answer is no.

A single same-saddle positive digit cloud can satisfy simultaneously

\[
E_{B_A(S_A)}(T_A)=\exp(-\omega(A))E_A,
\qquad
E_0(T_A)\asymp E_A,
\qquad
E_\eta(T_A)=o(E_A),
\qquad
|T_A|=o(E_A).
\tag{39}
\]

Moreover the positive exponential budget rate required for this can be made arbitrarily small through the sequence (3). The new source reservoir is not a remote coherent endpoint but a pair of leakage-scale critical chambers only `Theta(q^{-2})` away from the cancelled saddle.

This still does **not** construct a fatal Montgomery--Taylor near-extremizer or settle `ANF-099`. A global configuration containing this block must arrange the source cross term needed to bring total source energy back to the near-extremal affine floor while simultaneously retaining enough central-notch exposure. `ANF-097`, `ANF-119`, and `ANF-120` therefore remain the global completion constraints. What disappears is the proposed intermediate obstruction that a first exponential cancellation necessarily leaves an exponentially oversized reservoir requiring another layer merely to restore bounded macroscopic source mass.

The live positive gate is correspondingly sharper: one needs a global completion/coercivity principle that sees **bounded-macroscopic source blocks produced by critical exponential modulation**, not only a continuum rule forbidding source transport with exponential blowup. A negative completion would have to couple one of these notch-dark critical blocks to an admissible source-anti-aligned companion without losing the near-extremal denominator.

## 7. Prior-art and falsification audit

The finite geometric sum and the formula

\[
D_q(x)=e^{-\pi i(q-1)x}
\frac{\sin(\pi qx)}{\sin(\pi x)}
\]

are classical Dirichlet-kernel material. Powers of Dirichlet kernels and generalized Riesz products are also established harmonic-analysis subjects; for example Josef Obermaier, *Powers of the Dirichlet kernel with respect to orthogonal polynomials and related operators*, Acta Sci. Math. (Szeged) 83 (2017), 539--549, DOI `10.14232/actasm-016-072-z`, studies a different approximate-identity problem for powers of orthogonal-polynomial Dirichlet kernels. A targeted search also checked the standard Riesz-product literature. None of these sources supplies the coupled Montgomery--Taylor packet exponent (9), the critical root-leakage balance (16), the rate (3), or the physical translated-packet conclusion (39). No external theorem is load-bearing, so `research/analytic_frontier/SOURCES.md` does not need a new durable dependency.

Several failure modes were checked explicitly. The critical rate is not inferred by setting the fully coherent endpoint exponent to zero: that would give the much larger `Theta(q^{-2})` scale and misses the leakage maximum near the digit root. The ratio claim (27) uses nondegenerate critical maxima, not merely equality of exponential rates. Distinct physical points survive through the `O(A^{-4})` spacing perturbations. The central-notch bound uses the complete pointwise inequality `|D_q|<=q`, so it does not assume that the regenerated chamber is the only source maximum. Finally, the order of limits is essential: `q` is fixed during each `A->infinity` family, and no conclusion is asserted for a moving-arity diagonal where `rho_q` itself becomes subexponential in `A`.

No clue disposition changes. The accepted fixed-notch exposure-envelope clue remains the controlling scalar reduction; this finding strengthens the obstruction side by showing that the exponential branch already contains bounded-macroscopic-source, affine-negligible, notch-dark physical blocks rather than only oversized reservoirs.