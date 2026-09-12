# FD-076 — local Mertens maximal order forces power-dense physical source records

**Status:** `EXACT-DERIVED + LITERATURE-TRANSFER + LOCAL-MERTENS-MAXIMAL-ORDER + FLOOR-HARMONIC-INVERSION + POWER-WINDOW-SOURCE-RECURRENCE + RECORD-BLOCK-UPGRADE`.

`FD-072`--`FD-075` turn strict normalized records of the physical quotient-shell source into causal four-adic occupation, amplitude-length protected blocks, and growing same-parity large-radical swarms. Their remaining global weakness is record spacing: the internal power-frontier statement `FD-046` supplies arbitrarily large records but, by itself, permits them to be arbitrarily sparse.

A recent theorem of Pintz gives exactly the missing external input at the correct coarse scale. For the ordinary Mertens function

\[
\mathbf M(x)=\sum_{n\le x}\mu(n),
\]

Pintz proves that its maximum on every fixed power window has the full zeta-zero logarithmic order. The exact inverse floor-harmonic transform from `FD-046` transfers that local maximal-order statement to the physical source

\[
\mathcal H(N)=\sum_{n\le N}\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n.
\]

Let

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

For every fixed `lambda in (0,1)`, define

\[
S_{\mathcal H,\lambda}(X)
:=
\max_{X^{1-\lambda}\le n\le X}|\mathcal H(n)|.
\]

Then

\[
\boxed{
\lim_{X\to\infty}
\frac{\log(1+S_{\mathcal H,\lambda}(X))}{\log X}
=\Theta .
}
\tag{1}
\]

Thus the full physical-source power frontier occurs in **every fixed power window**, not merely on an unspecified limsup subsequence.

For `0<sigma<Theta`, put

\[
R_\sigma(n):=\frac{|\mathcal H(n)|}{n^\sigma},
\qquad
P_\sigma(X):=\max_{n\le X}R_\sigma(n).
\]

Equation (1) and the global upper frontier from `FD-046` give

\[
\boxed{
P_\sigma(X)=X^{\Theta-\sigma+o(1)}.
}
\tag{2}
\]

Since `Theta-sigma>0`, this forces strict records themselves to recur on the same power scale:

\[
\boxed{
\text{for every fixed }\lambda\in(0,1),
\text{ every sufficiently large }[X^{1-\lambda},X]
\text{ contains a strict }\sigma\text{-record.}
}
\tag{3}
\]

If `X_j` are the successive strict `sigma`-record indices, then

\[
\boxed{
\frac{\log X_{j+1}}{\log X_j}\longrightarrow1,
\qquad
|\mathcal H(X_j)|=X_j^{\Theta+o(1)}.
}
\tag{4}
\]

Under a false-RH frontier `Theta>1/2`, choose fixed `1/2<sigma<Theta`. The `FD-073` protected block attached to every sufficiently large record now has intrinsic radius

\[
A_j:=|\mathcal H(X_j)|=X_j^{\Theta+o(1)},
\tag{5}
\]

and `FD-075` upgrades uniformly to a same-parity large-radical cloud satisfying, for fixed admissible `eta,theta in (0,1)`,

\[
\boxed{
|Q_j|\ge X_j^{2\Theta-1-o(1)},
\qquad
\operatorname{rad}n\ge X_j^{\Theta-o(1)}
\quad(n\in Q_j).
}
\tag{6}
\]

Every point of this cloud still inherits the recentered causal occupation and Schur-defect lower bounds from `FD-073`. The previous statement that a false-RH record creates a large local swarm is therefore sharpened in two directions at once: the swarm exponent is controlled by the actual zero frontier `Theta`, and such record blocks cannot be separated by any fixed power gap.

This does **not** give bounded multiplicative record gaps or positive logarithmic density. The relation `X_(j+1)=X_j^(1+o(1))` still permits `X_(j+1)/X_j -> infinity`, and the logarithmic width of an amplitude block is only `A_j/X_j=X_j^(Theta-1+o(1))`. The accepted joint-occupation clue therefore remains open. The gain is a precise global recurrence theorem at power resolution, obtained by coupling new Mertens maximal-order literature to the exact source invertibility already present in the line.

## 1. Pintz supplies full Mertens power order in every fixed power window

Pintz defines, for any fixed `delta>0`,

\[
S_{\mathbf M,\delta}(X)
:=
\max_{X^{1-\delta}\le u\le X}|\mathbf M(u)|
\]

and proves in Theorem 2.2 of arXiv `2608.24878v2` that

\[
\log S_{\mathbf M,\delta}(X)
\sim
\log Z(X),
\tag{7}
\]

where

\[
Z(X):=\max_{\rho=\beta+i\gamma,\ \gamma>0}
\frac{X^\beta}{\gamma}.
\]

By the definition of the rightmost-zero frontier,

\[
\frac{\log Z(X)}{\log X}\longrightarrow\Theta:
\]

the upper bound follows from `beta<=Theta` and the positive lower height of nontrivial zeros, while for every `epsilon>0` one may fix a zero with `beta>Theta-epsilon` to obtain the reverse exponent. Hence Pintz's theorem yields

\[
\boxed{
\lim_{X\to\infty}
\frac{\log(1+S_{\mathbf M,\delta}(X))}{\log X}
=\Theta
}
\tag{8}
\]

for every fixed positive power-window parameter.

The use of Pintz is load-bearing here. Classical Phragmen/Littlewood omega results supply the global limsup exponent but do not by themselves say that a frontier-sized value occurs inside every fixed interval `[X^(1-delta),X]`.

## 2. Exact inverse floor-harmonic transport preserves the local exponent

`FD-046` proves the exact inverse identity

\[
\boxed{
\mathbf M(N)
=
\sum_{d\le N}\frac{\mu(d)}d
\mathcal H(\lfloor N/d\rfloor).
}
\tag{9}
\]

It also proves the global upper frontier: for every fixed `nu>0`,

\[
|\mathcal H(Y)|\ll_\nu Y^{\Theta+\nu}.
\tag{10}
\]

Fix `lambda in (0,1)` and set `a=lambda/4`. Apply (8) with Mertens window parameter `a`. Given sufficiently small `epsilon>0`, for every large `X` there is

\[
x\in[X^{1-a},X]
\]

such that

\[
|\mathbf M(x)|\ge X^{\Theta-\epsilon}.
\tag{11}
\]

Split (9) at

\[
K=x^a.
\]

Using (10) and `|mu(d)|<=1`, the tail satisfies

\[
\begin{aligned}
\sum_{d>K}\frac{|\mathcal H(\lfloor x/d\rfloor)|}{d}
&\ll_\nu
x^{\Theta+\nu}
\sum_{d>K}d^{-1-\Theta-\nu}\\
&\ll_{\nu,\Theta}
 x^{(\Theta+\nu)(1-a)}.
\end{aligned}
\tag{12}
\]

Choose `nu` and `epsilon` sufficiently small relative to the fixed quantity `a Theta`; then

\[
(\Theta+\nu)(1-a)<\Theta-\epsilon,
\]

so (12) is `o(X^(Theta-epsilon))`. Equations (9) and (11) therefore force

\[
\sum_{d\le K}
\frac{|\mathcal H(\lfloor x/d\rfloor)|}{d}
\ge \tfrac12 X^{\Theta-\epsilon}
\tag{13}
\]

for all sufficiently large `X`.

Every quotient in this head lies in the desired physical power window. Indeed,

\[
\frac{x}{d}
\ge x^{1-a}
\ge X^{(1-a)^2},
\]

and

\[
(1-a)^2=(1-\lambda/4)^2>1-\lambda.
\tag{14}
\]

The floor changes only an additive unit, so eventually

\[
X^{1-\lambda}
\le \lfloor x/d\rfloor\le X.
\]

Since

\[
\sum_{d\le K}\frac1d\ll\log X,
\]

(13) yields

\[
S_{\mathcal H,\lambda}(X)
\gg
\frac{X^{\Theta-\epsilon}}{\log X}.
\tag{15}
\]

As `epsilon` can be taken arbitrarily small, this proves the lower half of (1). The upper half follows immediately from (10). Thus the invertible floor transform preserves not just the global polynomial exponent from `FD-046`, but Pintz's fixed-power-window maximal exponent.

## 3. Prefix record heights have a full asymptotic power law

Fix `0<sigma<Theta`. Equation (1) gives, for any fixed `lambda`, a point `n<=X` with

\[
|\mathcal H(n)|\ge X^{\Theta-o(1)}.
\]

Since `n^sigma<=X^sigma`,

\[
P_\sigma(X)
\ge X^{\Theta-\sigma-o(1)}.
\tag{16}
\]

Conversely, (10) gives for every `nu>0`

\[
R_\sigma(n)
\ll_\nu n^{\Theta-\sigma+\nu}
\le X^{\Theta-\sigma+\nu}
\qquad(n\le X).
\tag{17}
\]

Combining (16)--(17) and letting `nu` tend to zero proves (2).

This is stronger than the earlier statement that `R_sigma` is merely unbounded when `sigma<Theta`. Its running maximum has a deterministic logarithmic growth exponent at every sufficiently large outer scale.

## 4. Fixed power gaps between strict records are impossible

Suppose for some fixed `lambda in (0,1)` that arbitrarily large windows `[X^(1-lambda),X]` contained no strict `sigma`-record. On such a window the running maximum would not change, so

\[
P_\sigma(X)
=
P_\sigma(\lfloor X^{1-\lambda}\rfloor).
\tag{18}
\]

But (2) gives

\[
\frac{\log P_\sigma(X)}{\log X}
\longrightarrow\Theta-\sigma,
\]

whereas

\[
\frac{\log P_\sigma(\lfloor X^{1-\lambda}\rfloor)}{\log X}
\longrightarrow
(1-\lambda)(\Theta-\sigma).
\tag{19}
\]

Because `Theta-sigma>0`, (18)--(19) are incompatible. This proves (3).

Let `X_j<X_(j+1)` be consecutive strict record indices. Apply (3) below `X_(j+1)`. For every fixed `lambda>0`, eventually the absence of a record between `X_j` and `X_(j+1)` forces

\[
X_j\ge X_{j+1}^{1-\lambda+o(1)}.
\]

Hence

\[
1\le
\limsup_j\frac{\log X_{j+1}}{\log X_j}
\le\frac1{1-\lambda}.
\]

Letting `lambda downarrow0` proves the first assertion in (4).

At a strict record index,

\[
R_\sigma(X_j)=P_\sigma(X_j).
\]

Equation (2) therefore gives

\[
R_\sigma(X_j)
=X_j^{\Theta-\sigma+o(1)},
\]

and multiplication by `X_j^sigma` proves the amplitude statement in (4).

## 5. The protected false-RH blocks inherit the actual zero-frontier exponent

Assume `Theta>1/2` and fix `1/2<sigma<Theta`. The successive strict `sigma`-records are now power-dense by (3)--(4), and their amplitudes satisfy (5).

`FD-073` says that, for every fixed `eta in (0,1)`, the whole additive neighborhood

\[
|Y-X_j|\le\eta A_j
\]

consists of quantitative near-records whose recentered horizons `T=4Y`, `D=3` have a uniform positive nonsquarefree occupation and Schur defect. Equation (5) therefore pins the protected block radius to

\[
X_j^{\Theta+o(1)}.
\tag{20}
\]

`FD-075` further gives, for every fixed `theta in (0,1)`, at least a constant multiple of

\[
\frac{A_j^2}{X_j}
\]

same-parity coefficient hosts in the backward part of the block, each with radical bounded below by a constant multiple of `A_j`. Inserting (5) yields the safe one-sided exponent formulation (6): for every fixed `epsilon>0`, eventually

\[
|Q_j|\gg X_j^{2\Theta-1-\epsilon},
\qquad
\operatorname{rad}n\gg X_j^{\Theta-\epsilon}.
\tag{21}
\]

Since `2Theta-1>0`, the arithmetic cloud grows polynomially with an exponent determined by the true zero frontier rather than by the auxiliary record normalization exponent `sigma`.

This removes two freedoms from a negative recurrence model. It can no longer choose record amplitudes far below the frontier exponent, and it cannot place consecutive record blocks across a fixed power gap. It may still use subpower multiplicative gaps large enough to keep the shrinking additive blocks globally sparse.

## 6. Falsification boundary and prior-art audit

The conclusion is deliberately **power-scale**, not ordinary multiplicative recurrence. The relation

\[
\frac{\log X_{j+1}}{\log X_j}\to1
\]

is compatible with `X_(j+1)/X_j -> infinity`; for example, a gap of size `exp(sqrt(log X_j))` is invisible at this resolution. When `Theta<1`, the protected block has relative width

\[
\frac{A_j}{X_j}=X_j^{\Theta-1+o(1)}\to0,
\]

so (3)--(6) do not imply positive ordinary density, positive logarithmic density, overlap of consecutive protected blocks, or a global positive lower bound for `U/E`.

The external theorem is also source-specific. Pintz's result is for the ordinary Mertens function. Equation (1) for `mathcal H` is not quoted from the literature; it is obtained here by combining Pintz's local maximum theorem with the exact inverse floor transform (9) and the already-established global source frontier. A search for the coefficient Dirichlet series `zeta(s+1)/zeta(s)` and the summatory coefficients `mu(rad n) phi(rad n)/n` did not locate a published fixed-power-window maximal-order statement for this physical source. No priority claim is made from that search.

The load-bearing literature dependency is János Pintz, *Oscillation of partial sums of the Möbius function and zeros of Riemann's zeta function*, arXiv `2608.24878v2` (2026), especially Theorem 2.2. It is recorded in `SOURCES.md`. No assumption beyond that theorem and the exact internal identities of `FD-046`, `FD-073`, and `FD-075` is used.

The durable frontier change is therefore precise: the record-protection route no longer needs a new theorem merely to exclude fixed power gaps. What remains is a **subpower recurrence problem**: determine whether the exact physical coefficient law can improve `X_(j+1)=X_j^(1+o(1))` to enough ordinary/logarithmic recurrence that the `X_j^(Theta+o(1))` protected blocks, or their `X_j^(2Theta-1-o(1))` arithmetic swarms, force a global same-horizon occupation statement.
