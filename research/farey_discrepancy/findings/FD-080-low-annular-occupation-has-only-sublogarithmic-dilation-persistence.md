# FD-080 — low annular occupation has only sublogarithmic dilation persistence

**Status:** `EXACT-DERIVED + ANNULAR-DILATION + FIRST-PASSAGE + SUBLOGARITHMIC-PERSISTENCE + SUBPOWER-RECURRENCE + EXCEPTIONAL-SCALE-LOCALIZATION + SCHUR-PROJECTIVE-TRANSFER`.

`FD-079` proves that the energy-weighted nonsquarefree occupation of every fixed power annulus has a finite logarithmic entropy budget. That gives constant-strength recurrence on a positive logarithmic proportion of endpoints, but positive logarithmic density alone still allows very long exceptional deserts placed sparsely enough.

The full annular energy exponent from `FD-078` rules out that remaining geometry along the exact dilation successor hidden inside `FD-079`. A low-occupation endpoint forces a definite multiplicative increase of the annular energy relative to its exact predecessor. If that happened for a positive logarithmic number of consecutive dilation steps, the accumulated increase would exceed the already-known exponent `2 Theta`. Therefore every sufficiently large endpoint reaches a constant-strength occupied descendant after only `o(log X)` exact dilation steps. Equivalently, constant annular occupation reappears after a **subpower multiplicative enlargement**.

Fix a Schur head `D>=1`, a power-annulus parameter `0<alpha<1`, and a nonsquarefree integer `q>1`. Retain the notation of `FD-078`--`FD-079`:

\[
A(X):=\mathscr E_{D,\alpha}(X),
\qquad
B(X):=\mathscr U_{D,\alpha}(X),
\qquad
\Omega(X):=\frac{B(X)}{A(X)},
\]

\[
w(q):=\frac{J_2(q)}{q^2},
\qquad
c_q:=w(q)q^{-2\Theta},
\]

where

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

For an integer endpoint `X`, define the exact successor

\[
S_q(X):=q(X+1),
\tag{1}
\]

and its orbit

\[
X_0:=X,
\qquad
X_{j+1}:=S_q(X_j).
\tag{2}
\]

For every fixed threshold

\[
0<\eta<c_q,
\tag{3}
\]

let

\[
\tau_\eta(X)
:=
\min\{j\ge1:\Omega(X_j)>\eta\}.
\tag{4}
\]

Then, for all sufficiently large `X`, the minimum exists and

\[
\boxed{
\tau_\eta(X)=o(\log X).
}
\tag{5}
\]

Consequently, if

\[
Y_X:=X_{\tau_\eta(X)},
\]

then

\[
\boxed{
\Omega(Y_X)>\eta,
\qquad
\frac{\log Y_X}{\log X}\longrightarrow1,
\qquad
\frac{Y_X}{X}=X^{o(1)}.
}
\tag{6}
\]

Equivalently, for every fixed `epsilon>0`, all sufficiently large `X` admit an integer endpoint `Y` on the exact successor orbit (2) such that

\[
\boxed{
X<Y\le X^{1+\epsilon},
\qquad
\Omega_{D,\alpha}(Y)>\eta.
}
\tag{7}
\]

Thus the zero-log-density exceptional endpoints still allowed by `FD-079` cannot form a bad desert spanning any fixed positive amount of logarithmic scale. They may be arbitrarily deep and may occur infinitely often, but constant-strength annular occupation must return before any fixed-power enlargement of the starting endpoint.

For `q=4`, `w(4)=3/4` and `Theta<=1`, so

\[
c_4=\frac34\,4^{-2\Theta}\ge\frac3{64}.
\tag{8}
\]

Hence the following fully unconditional specialization is available: for every fixed

\[
0<\eta<\frac3{64}
\]

and every `epsilon>0`, every sufficiently large `X` has a four-adic successor descendant `Y<=X^(1+epsilon)` with

\[
\boxed{
\Omega_{D,\alpha}(Y)>\eta.
}
\tag{9}
\]

Under RH the admissible threshold extends to every `eta<3/16`.

## 1. The exact successor turns annular occupation loss into forced energy growth

`FD-079` defines

\[
P_q(T):=\left\lfloor\frac Tq\right\rfloor-1
\]

and proves, for all sufficiently large endpoints,

\[
\boxed{
B(T)\ge w(q)A(P_q(T)).
}
\tag{10}
\]

The successor (1) is chosen so that the predecessor is exact:

\[
P_q(S_q(X))
=
\left\lfloor\frac{q(X+1)}q\right\rfloor-1
=X.
\tag{11}
\]

Therefore

\[
\boxed{
B(X_{j+1})\ge w(q)A(X_j).
}
\tag{12}
\]

If the next endpoint is bad at threshold `eta`, meaning

\[
\Omega(X_{j+1})\le\eta,
\]

then (12) forces

\[
\eta A(X_{j+1})
\ge B(X_{j+1})
\ge w(q)A(X_j),
\]

and hence

\[
\boxed{
\frac{A(X_{j+1})}{A(X_j)}
\ge\frac{w(q)}\eta.
}
\tag{13}
\]

Thus every bad successor consumes a fixed amount of the available logarithmic growth budget. If the first `m` successors are all bad, multiplication of (13) gives

\[
\boxed{
A(X_m)
\ge
\left(\frac{w(q)}\eta\right)^m A(X).
}
\tag{14}
\]

This is stronger information than the endpoint-density statement of `FD-079`: it attaches a deterministic energy-growth price to a **contiguous run on one exact causal successor orbit**.

## 2. The full `2 Theta` exponent makes every bad run sublogarithmic

`FD-078` proves the full limit

\[
\boxed{
\frac{\log A(T)}{\log T}\longrightarrow2\Theta.
}
\tag{15}
\]

The distinction between a full limit and a mere upper envelope is load-bearing here. Put

\[
F(T):=\log A(T),
\qquad
G(T):=F(T)-2\Theta\log T.
\tag{16}
\]

Then

\[
G(T)=o(\log T).
\tag{17}
\]

The affine recurrence (2) has the exact closed form

\[
X_j+\frac{q}{q-1}
=
q^j\left(X+\frac{q}{q-1}\right).
\tag{18}
\]

Consequently, uniformly for `j>=1`,

\[
\boxed{
\log X_j-\log X
=j\log q+O_q(X^{-1}).
}
\tag{19}
\]

Suppose the first `m` descendants are bad. Taking logarithms in (14), then using (16)--(19), gives

\[
m\log\frac{w(q)}\eta
\le
F(X_m)-F(X)
\]

and therefore

\[
\boxed{
\delta_\eta m
\le
G(X_m)-G(X)+O_q(X^{-1}),
}
\tag{20}
\]

where

\[
\delta_\eta
:=
\log\frac{w(q)}\eta-2\Theta\log q
=
\log\frac{c_q}{\eta}
>0.
\tag{21}
\]

For a quantitative tail form, define

\[
r(X)
:=
\sup_{T\ge X}
\left|
\frac{F(T)}{\log T}-2\Theta
\right|.
\tag{22}
\]

By (15), `r(X)->0`. Since every `X_j>=X`, equations (19)--(20) imply

\[
\bigl(\delta_\eta-r(X)\log q\bigr)m
\le
2r(X)\log X+o(\log X)+O_q(1).
\tag{23}
\]

For sufficiently large `X`, the coefficient on the left is positive. Hence every all-bad prefix satisfies

\[
\boxed{
\frac{m}{\log X}
\le
\frac{2r(X)+o(1)}
{\delta_\eta-r(X)\log q}
\longrightarrow0.
}
\tag{24}
\]

An infinite bad tail is impossible for the same reason, so `tau_eta(X)` exists; applying (24) to the maximal bad prefix proves (5).

The threshold `eta<c_q` is exact for this drift argument. At `eta=c_q`, the positive drift `delta_eta` in (21) vanishes, and the `2 Theta` exponent alone no longer prevents a long sequence of steps whose energy growth matches the frontier rate exactly.

## 3. Sublogarithmic first passage is the same as subpower scale recurrence

Let `Y_X=X_(tau_eta(X))`. Equation (19) and (5) give

\[
\log\frac{Y_X}{X}
=
\tau_\eta(X)\log q+O_q(X^{-1})
=o(\log X).
\tag{25}
\]

This proves (6). In particular, for every fixed `epsilon>0`, eventually

\[
\log\frac{Y_X}{X}
<\epsilon\log X,
\]

which is exactly `Y_X<X^(1+epsilon)` and proves (7).

A useful equivalent formulation is the **absence of fixed-power bad deserts**. Fix `eta<c_q` and `epsilon>0`. There is no unbounded sequence `X_n` for which

\[
\Omega_{D,\alpha}(T)\le\eta
\]

at every integer endpoint

\[
X_n<T\le X_n^{1+\epsilon}.
\]

Indeed, the exact successor descendant supplied by (7) lies inside that interval and has occupation above `eta`.

The same recurrence holds for the annular Schur projective defect

\[
\Pi_{D,\alpha}(T)
:=
\frac{\mathscr R_{D,\alpha}(T)}
{\mathscr E_{D,\alpha}(T)},
\]

because `FD-078` gives `Pi>=Omega` endpointwise. Thus every sufficiently large scale reaches a constant projective gap after a subpower multiplicative enlargement as well.

## 4. What this adds beyond logarithmic density

A set of endpoints can have positive lower logarithmic density and still contain sparse gaps whose logarithmic length is a fixed positive fraction of their starting scale. Therefore the positive-proportion recurrence in `FD-079` does not by itself imply (7).

The new input is the conjunction of two facts that previously played separate roles: `FD-079` supplies the exact one-step predecessor injection, while `FD-078` says the annular energy has a **full**, not merely limsup, exponent `2 Theta`. A long consecutive bad run would force an energy exponent strictly larger than `2 Theta`, with excess per step exactly

\[
\delta_\eta=\log(c_q/\eta).
\]

This directly addresses the exceptional-scale localization frontier left by `FD-079`. The remaining exceptional set can still contain arbitrarily bad individual endpoints, but no such endpoint can initiate a constant-threshold failure that persists through a fixed-power future window.

The accepted clue `CLUE-joint-nonsquarefree-jordan-energy-occupation` remains open. The present theorem concerns the annular energy-weighted ratio `Omega_(D,alpha)`, not the horizon-level ratio

\[
\nu_{H,D}=\frac{U_{H,D}}{E_{H,D}}.
\]

It therefore supplies stronger recurrence currency for the aggregated physical geometry without promoting that recurrence to an eventual pointwise occupation theorem.

## 5. Stress tests and boundary of the claim

The theorem does **not** give a bounded number of dilation steps. The only input controlling the error in (15) is `r(X)->0`, with no rate. Consequently `tau_eta(X)` may still diverge, for example on an abstract profile whose subleading logarithmic energy term has excursions of size `o(log X)`. The conclusion `tau=o(log X)` is the sharp scale forced by the information used here; improving it to `O(1)` or even `O(log log X)` would require a quantitative remainder in the annular energy asymptotic or additional arithmetic rigidity.

Likewise, (7) does not eliminate isolated deep dips, does not give positive natural density of good endpoints, and does not prevent bad runs over multiplicative factors `X^(o(1))`. It only proves that those runs cannot reach any fixed power `X^epsilon`.

The fixed parameters are essential. The proof keeps `D`, `alpha`, and `q` fixed. The exact annular injection from `FD-079` uses fixed `alpha>0` to fit complete `q`-blocks inside the target annulus, and it uses integral nonsquarefree `q` both for exact floor predecessor blocks and for row membership in `U`. A varying head or a shrinking annulus requires a different argument.

The result is source-specific through `FD-078`. The matched synthetic escapes behind `FD-048` are not contradicted: the present first-passage conclusion uses the Pintz-driven full annular physical-energy exponent established later in `FD-078`, which those generic one-Lipschitz controls were never required to satisfy.

Finally, the theorem is not an RH proof and does not improve the Mertens exponent. It restricts the geometry of any surviving Farey/Schur obstruction by showing that constant-strength transverse occupation is **power-syndetic in the future multiplicative scale**, even though eventual pointwise occupation remains unproved.

## 6. Prior-art boundary

No new external theorem is used. The load-bearing inputs are the exact annular dilation inequality of `FD-079` and the full physical annular-energy exponent of `FD-078`, whose external dependencies are already anchored in `SOURCES.md`.

A targeted literature search over Farey discrepancy, Mertens-function formulations, Jordan-totient/GCD quadratic forms, nonsquarefree restrictions, logarithmic-density statements, and multiplicative recurrence found the expected modern local-discrepancy work of Rogelio Tomás García and classical Farey--Mertens material, but no result matching this specific first-passage consequence for the physical nonsquarefree Jordan energy. The argument above is elementary once `FD-078` and `FD-079` are available, so no broad literature novelty claim is made and `SOURCES.md` requires no new anchor.

The decisive falsification points are transparent. If (10) failed on the exact successor, the forced step growth (13) would disappear. If the annular energy had only a limsup exponent rather than the full limit (15), long bad runs could hide inside low-energy stretches. If `eta>=c_q`, the positive drift in (21) is unavailable. Subject to those boundaries, the first-passage and subpower-recurrence conclusions follow exactly.
