# FD-073 — power-record protection propagates through amplitude-length causal blocks

**Status:** `EXACT-DERIVED + SOURCE-POWER-RECORDS + ONE-LIPSCHITZ-PROPAGATION + NEAR-RECORD-BLOCKS + CAUSAL-FOUR-ADIC-OCCUPATION + CRITICAL-ENDPOINT-QUANTIFICATION + FALSE-RH-THICKENED-RECORD-SUBSEQUENCE`.

`FD-072` protects the single causal horizon `T=4X` attached to a normalized source power record `X`, but leaves the record set potentially arbitrarily sparse. The physical shell source has an additional exact rigidity from `FD-033`/`FD-037`: its increments have absolute value at most one. That rigidity propagates a record to an entire additive neighborhood before any number-theoretic spacing theorem is used.

Let

\[
R_\sigma(n):=\frac{|\mathcal H(n)|}{n^\sigma},
\qquad
M_\sigma(Y):=\max_{1\le n\le Y}R_\sigma(n),
\tag{1}
\]

with `sigma>=1/2`, and let `X` be a nonzero `sigma`-record,

\[
A:=|\mathcal H(X)|>0,
\qquad
R_\sigma(X)=M_\sigma(X).
\tag{2}
\]

For an integer `Y>=1`, write `h:=|Y-X|`. If `h<A`, then

\[
\boxed{
\frac{R_\sigma(Y)}{M_\sigma(Y)}
\ge
c_{X,h,\sigma}
:=
\frac{A-h}{A+h}
\left(\frac{X}{X+h}\right)^\sigma.
}
\tag{3}
\]

Thus every point within additive distance less than the record amplitude is itself a quantitative near-record. In particular, for any fixed `0<eta<1` and every integer

\[
|Y-X|\le \eta A,
\tag{4}
\]

one has, using `A<=X`,

\[
\boxed{
\frac{R_\sigma(Y)}{M_\sigma(Y)}
\ge
c_{\eta,\sigma}
:=
\frac{1-\eta}{(1+\eta)^{1+\sigma}}>0.
}
\tag{5}
\]

The `FD-072` causal four-adic argument therefore applies uniformly throughout this whole neighborhood. Put

\[
\mathscr C_\sigma(Y)
:=
\sum_{r=4}^{4Y}\left(\frac4r\right)^{2\sigma}.
\tag{6}
\]

Then every `Y` satisfying (4) obeys

\[
\boxed{
\nu_{4Y,3}
:=\frac{U_{4Y,3}}{E_{4Y,3}}
\ge
\frac{3c_{\eta,\sigma}^2}{4\mathscr C_\sigma(Y)}.
}
\tag{7}
\]

Consequently, if `sigma>1/2`, with the convergent constant

\[
\mathscr C_\sigma
:=
\sum_{r=4}^{\infty}\left(\frac4r\right)^{2\sigma},
\qquad
\kappa_\sigma:=\frac3{4\mathscr C_\sigma},
\tag{8}
\]

we obtain the uniform block estimate

\[
\boxed{
|Y-X|\le\eta A
\quad\Longrightarrow\quad
\nu_{4Y,3}
\ge
c_{\eta,\sigma}^2\kappa_\sigma.
}
\tag{9}
\]

The same block has the Schur consequences

\[
\boxed{
\varepsilon_{4Y,3}
\ge c_{\eta,\sigma}^2\kappa_\sigma,
\qquad
\mathfrak D_{4Y,3}
\ge
\frac{c_{\eta,\sigma}^2\kappa_\sigma}{24}.
}
\tag{10}
\]

At the critical endpoint `sigma=1/2`, the constant occupation of `FD-072` is unavailable, but the finite-horizon form gives an explicit logarithmic replacement:

\[
\mathscr C_{1/2}(Y)
=4\sum_{r=4}^{4Y}\frac1r
=4\bigl(H_{4Y}-H_3\bigr),
\tag{11}
\]

and hence

\[
\boxed{
\nu_{4Y,3}
\ge
\frac{3c_{\eta,1/2}^2}
{16\bigl(H_{4Y}-H_3\bigr)}
\asymp_\eta \frac1{\log Y}
}
\tag{12}
\]

through the same amplitude-length neighborhood of every nonzero `1/2`-record. This does not produce a critical-line gap, but it makes the degeneration in `FD-072` quantitative rather than merely saying that the infinite comparison series diverges.

Under a false-RH frontier `Theta>1/2`, choose fixed

\[
\frac12<\sigma<\Theta.
\tag{13}
\]

By `FD-046` and `FD-072`, the strict `sigma`-record values are unbounded. Along the strict record sequence `X_j`, therefore,

\[
\frac{A_j}{X_j^\sigma}
=R_\sigma(X_j)
\longrightarrow\infty.
\tag{14}
\]

For every fixed `eta in (0,1)`, each record consequently generates a protected source block

\[
I_j
:=
\{Y\in\mathbb N:|Y-X_j|\le\eta A_j\}
\tag{15}
\]

with

\[
\boxed{
|I_j|\asymp_\eta A_j,
\qquad
\frac{|I_j|}{X_j^\sigma}\longrightarrow\infty,
\qquad
\inf_{Y\in I_j}\nu_{4Y,3}
\ge c_{\eta,\sigma}^2\kappa_\sigma>0.
}
\tag{16}
\]

Thus the protected false-RH-facing episodes from `FD-072` are not isolated points. Every record thickens automatically into a polynomially long additive block whose length exceeds `X_j^sigma` by an unbounded factor. No short-interval Möbius theorem, record-spacing theorem, or delayed reciprocal-host construction is required.

## 1. The physical source makes a record stable for one amplitude in either direction

`FD-033`/`FD-037` give the exact coefficient representation

\[
\mathcal H(N)=\sum_{n\le N}c(n),
\qquad
c(n)=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n,
\tag{17}
\]

with `|c(n)|<=1`. Hence

\[
|\mathcal H(u)-\mathcal H(v)|\le |u-v|
\tag{18}
\]

for all nonnegative integers `u,v`, and since `mathcal H(0)=0`,

\[
A=|\mathcal H(X)|\le X.
\tag{19}
\]

Fix `Y` and `h=|Y-X|<A`. Equation (18) gives

\[
|\mathcal H(Y)|\ge A-h.
\tag{20}
\]

We next bound the normalized prefix maximum at `Y`. If `Y<=X`, then

\[
M_\sigma(Y)\le M_\sigma(X)=\frac A{X^\sigma}
\le\frac{A+h}{X^\sigma}.
\tag{21}
\]

If `Y>X`, the record condition gives the same bound `A/X^sigma` for every `n<=X`, while for `X<n<=Y`, (18) gives

\[
|\mathcal H(n)|\le A+(n-X)\le A+h,
\]

and `n>=X`. Thus in either case

\[
\boxed{
M_\sigma(Y)\le\frac{A+h}{X^\sigma}.
}
\tag{22}
\]

Also `Y<=X+h`, so from (20)

\[
R_\sigma(Y)
\ge
\frac{A-h}{(X+h)^\sigma}.
\tag{23}
\]

Dividing (23) by (22) proves (3). If `h<=eta A`, then (19) yields

\[
\frac{A-h}{A+h}\ge\frac{1-\eta}{1+\eta},
\qquad
\frac X{X+h}\ge\frac1{1+\eta},
\tag{24}
\]

which proves (5).

The two-sided formulation is useful: it is not a statement that the future source cannot create a larger record eventually. It says only that bounded increments prevent a record from losing a fixed fraction of its normalized dominance before one travels a distance comparable with its own amplitude.

## 2. Any quantitative near-record inherits the causal denominator bound

The propagation above is independent of the Jordan geometry. The second step is a reusable strengthening of `FD-072`.

Suppose at some `Y` one has

\[
R_\sigma(Y)\ge c\,M_\sigma(Y)
\qquad(0<c\le1).
\tag{25}
\]

Then for every `1<=n<=Y`,

\[
\frac{|\mathcal H(n)|}{n^\sigma}
\le M_\sigma(Y)
\le c^{-1}\frac{|\mathcal H(Y)|}{Y^\sigma},
\]

hence

\[
\boxed{
|\mathcal H(n)|
\le
c^{-1}|\mathcal H(Y)|
\left(\frac nY\right)^\sigma.
}
\tag{26}
\]

At the causal horizon `T=4Y`, `D=3`, every surviving quotient satisfies

\[
n_r:=\left\lfloor\frac{4Y}{r}\right\rfloor\le Y.
\tag{27}
\]

With `w(r)=J_2(r)/r^2<=1`, equations (26)--(27) give

\[
\begin{aligned}
E_{4Y,3}
&=\sum_{r=4}^{4Y}w(r)\mathcal H(n_r)^2\\
&\le
c^{-2}|\mathcal H(Y)|^2
\sum_{r=4}^{4Y}\left(\frac4r\right)^{2\sigma}\\
&=
\boxed{c^{-2}\mathscr C_\sigma(Y)|\mathcal H(Y)|^2}.
\end{aligned}
\tag{28}
\]

The nonsquarefree row `r=4` still samples the endpoint exactly,

\[
n_4=Y,
\qquad
w(4)=\frac34,
\]

so

\[
U_{4Y,3}\ge\frac34|\mathcal H(Y)|^2.
\tag{29}
\]

Dividing (29) by (28) proves (7), and (5) gives the record-neighborhood version. For `sigma>1/2`, replacing the finite sum by the convergent infinite sum proves (9).

As in `FD-072`, every nonsquarefree Jordan coordinate is transverse to the Schur equality ray, so `epsilon>=nu`. Also

\[
\Delta_{4Y,3}=C_{4Y}-C_3\ge\frac1{J_2(5)}=\frac1{24}
\tag{30}
\]

for `Y>=2`. This proves (10). For the finitely many tiny values where the displayed head comparison is not needed, the block statement can simply be read at sufficiently large records; all asymptotic consequences concern `X_j->infinity`.

## 3. The critical endpoint loses only a harmonic factor in this mechanism

`FD-072` deliberately stopped at `sigma>1/2`, because the infinite denominator majorant diverges at the endpoint. For a fixed physical horizon, however, only `r<=4Y` occurs. At `sigma=1/2`, (6) becomes exactly (11), and inserting it into (7) proves (12).

This is a boundary statement, not a critical-line theorem. A `1/2`-record need not occur with any useful density, its amplitude need not exceed `sqrt(X)` by an unbounded factor under RH, and the lower bound itself still decays like `1/log Y`. The point is narrower: the causal record mechanism does not collapse discontinuously at `1/2`; its exact finite-horizon loss is harmonic.

For `sigma>1/2`, the infinite sum is bounded and the same construction gives a constant block gap. The transition between the two regimes is therefore transparent in the same formula `mathscr C_sigma(Y)` rather than hidden in separate arguments.

## 4. False RH thickens the protected set, but does not control its global density

If `Theta>sigma>1/2`, `FD-046` transfers the zeta-zero power frontier to `mathcal H`. Hence `R_sigma(n)` is unbounded. At successive strict records its values increase to infinity, proving (14).

Equation (16) is then stronger than the singleton conclusion of `FD-072`: the number of protected neighboring source times around each record is not merely divergent but larger than `X_j^sigma` by an unbounded factor. Corresponding physical horizons `T=4Y` occupy an additive interval of the same order.

This still does **not** solve the accepted joint-occupation clue. The gaps between successive records may be much larger than `A_j`; the blocks `I_j` may have zero ordinary or logarithmic density; and `A_j/X_j` may tend to zero. In particular, (16) cannot be summed into a global occupation theorem without new information on record spacing, overlap, or a propagation mechanism extending farther than the one-Lipschitz amplitude scale.

The result instead removes one weaker escape from the frontier: source-selected protected episodes cannot be literally pointlike. Any future spacing argument may now work with blocks of intrinsic radius `asymp |mathcal H(X_j)|`, not isolated record locations.

## 5. Stress tests and evidence boundary

The proof uses absolute values throughout, so sign changes of `mathcal H` cause no hidden monotonicity assumption. The restriction `h<A` is essential: once the displacement reaches the amplitude, the one-Lipschitz lower bound (20) can vanish and no near-record statement follows. The horizon is re-centered separately at each nearby point as `T=4Y`; keeping the original horizon `4X` while moving the source point would not preserve the exact row-4 sample and is not claimed.

The same-source condition is also essential. Equation (25) must refer to the exact `mathcal H` sampled in the denominator. A record of `M`, a smoothed surrogate, or a fitted envelope cannot be substituted without a proved transfer. Likewise, (16) gives additive thickness only; interpreting it as positive density would be false without a record-spacing theorem.

A finite sanity check of the coefficient identity confirms the exact unit increment bound, but no numerical record experiment is used in the proof. The argument is deterministic once (17) and the existing Schur/Jordan representation are given.

## 6. Prior-art boundary and consequences

A targeted audit covered Mertens record/extremal computations, normalized Mertens distributions, and recent Farey local-discrepancy formulas. Computational work such as Greg Hurst's record/extremal studies concerns values and algorithms for the Mertens function, while the Farey literature located in the audit concerns rank/local-discrepancy formulas and classical Mertens bridges. No source located supplies the particular implication used here: a normalized power record of the physical shell source, combined with its exact unit increment law, produces an amplitude-length family of near-records whose own four-adic causal horizons have a uniform nonsquarefree Schur-energy fraction. No novelty claim is made for record processes, Lipschitz persistence, harmonic sums, or Mertens computations separately.

No new external theorem is load-bearing. The zeta-frontier consequence uses only the Titchmarsh/Littlewood anchor already recorded in `SOURCES.md` and transferred internally by `FD-046`; the propagation itself is elementary. Therefore `SOURCES.md` requires no update.

The durable consequence is the quantitative replacement of the `FD-072` singleton picture:

\[
\boxed{
\text{power record at }X
\quad\Longrightarrow\quad
\text{protected causal block of radius }\asymp |\mathcal H(X)|.
}
\]

For a false-RH frontier and any fixed `1/2<sigma<Theta`, those radii exceed `X^sigma` by an unbounded factor along the strict-record sequence. The next missing theorem is correspondingly sharper: control the **gaps between these amplitude-length blocks**, or prove a mechanism that propagates causal denominator control beyond one source amplitude. Merely proving that records exist infinitely often is no longer the relevant bottleneck.
