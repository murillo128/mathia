# FD-077 — Pintz average order forces full-counting-exponent physical source abundance

**Status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + AVERAGE-ORDER-TRANSFER + POWER-ANNULUS-L1-MASS + FULL-COUNTING-EXPONENT + CAUSAL-NONSQUAREFREE-OCCUPATION + FRONTIER-UPGRADE`.

`FD-076` transfers Pintz's fixed-power-window maximal-order theorem from the ordinary Mertens function to the physical quotient-shell source

\[
\mathcal H(N)
=\sum_{s\le N}\frac{\mathbf M(\lfloor N/s\rfloor)}s,
\]

and obtains strict normalized source records in every fixed power window. That is already much stronger than an isolated limsup statement, but the resulting record sequence can still have unbounded multiplicative gaps and therefore need not give positive ordinary or logarithmic density of protected record blocks.

Pintz's 2026 theorem contains another input that is more useful for abundance than for records: the average absolute order

\[
D_M(X)=\frac1X\int_0^X|\mathbf M(u)|\,du
\]

has the full zeta-zero power exponent. Combining that average theorem with the **inverse** floor-harmonic identity of `FD-046` gives a stronger physical conclusion than `FD-076`: the logarithmic `L^1` mass of `mathcal H` has exponent `Theta` in every fixed power annulus, and values within an arbitrary fixed power of the frontier occur on a set of **full polynomial counting exponent one**.

Moreover, any fixed nonsquarefree Jordan row converts those abundant source values into causal horizons whose nonsquarefree occupation and normalized Schur projective defect lose at most an arbitrarily small polynomial power. Thus the false-RH-facing physical signal is not merely power-dense through sparse records: it is present on `X^(1-o_power(1))` causal samples at every arbitrarily small polynomial tolerance.

Let

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

Define

\[
L_{\mathcal H}(X)
:=
\sum_{n\le X}\frac{|\mathcal H(n)|}{n}
\]

and, for fixed `0<lambda<1`,

\[
L_{\mathcal H}(X;\lambda)
:=
\sum_{X^{1-\lambda}<n\le X}
\frac{|\mathcal H(n)|}{n}.
\]

Then

\[
\boxed{
\lim_{X\to\infty}
\frac{\log(1+L_{\mathcal H}(X))}{\log X}
=\Theta,
}
\tag{1}
\]

and, for every fixed `lambda in (0,1)`,

\[
\boxed{
\lim_{X\to\infty}
\frac{\log(1+L_{\mathcal H}(X;\lambda))}{\log X}
=\Theta.
}
\tag{2}
\]

For every fixed `kappa>0`, put

\[
N_\kappa(X)
:=
\#\left\{
 n\le X:
 |\mathcal H(n)|\ge X^{\Theta-\kappa}
\right\}.
\]

Then

\[
\boxed{
\lim_{X\to\infty}
\frac{\log(1+N_\kappa(X))}{\log X}
=1.
}
\tag{3}
\]

So frontier-near source values have full polynomial counting exponent. This does **not** assert positive natural density: a set may have counting exponent one while its density tends to zero.

Now fix a Schur head `D`, and choose any fixed nonsquarefree integer `q>D`. With

\[
E_{H,D}
=\sum_{D<r\le H}w(r)
\mathcal H(\lfloor H/r\rfloor)^2,
\qquad
U_{H,D}
=\sum_{\substack{D<r\le H\\\mu(r)=0}}w(r)
\mathcal H(\lfloor H/r\rfloor)^2,
\]

\[
w(r)=\frac{J_2(r)}{r^2},
\qquad
\nu_{H,D}=\frac{U_{H,D}}{E_{H,D}},
\]

and with `epsilon_(H,D)` denoting the normalized Schur projective defect of `FD-049`, define for fixed `eta>0`

\[
\mathscr G_{\eta,D,q}(X)
:=
\left\{
 n\le X:
 |\mathcal H(n)|\ge X^{\Theta-\eta/8},\ 
 \nu_{qn,D}\ge X^{-\eta},\
 \varepsilon_{qn,D}\ge X^{-\eta}
\right\}.
\]

Then

\[
\boxed{
\lim_{X\to\infty}
\frac{\log(1+\#\mathscr G_{\eta,D,q}(X))}{\log X}
=1.
}
\tag{4}
\]

Equation (4) is the main physical consequence. Under false RH, choose `eta` so small that `Theta-eta/8>1/2`; then a full-counting-exponent family of causal horizons simultaneously carries a genuinely off-critical-size source sample and avoids every prescribed fixed polynomial rate of nonsquarefree/projective saturation loss.

## 1. The inverse floor transform converts Mertens average mass into logarithmic source mass

`FD-046` proves the exact inverse identity

\[
\boxed{
\mathbf M(N)
=
\sum_{d\le N}
\frac{\mu(d)}d
\mathcal H(\lfloor N/d\rfloor).
}
\tag{5}
\]

Take absolute values and sum over integers `N<=X`. Since `|mu(d)|<=1`,

\[
\sum_{N\le X}|\mathbf M(N)|
\le
\sum_{d\le X}\frac1d
\sum_{N=d}^{X}
|\mathcal H(\lfloor N/d\rfloor)|.
\tag{6}
\]

For fixed `d`, every quotient value `m=floor(N/d)` occurs at most `d` times. Therefore

\[
\begin{aligned}
\sum_{N\le X}|\mathbf M(N)|
&\le
\sum_{d\le X}
\sum_{m\le X/d}|\mathcal H(m)|\\
&=
\sum_{m\le X}|\mathcal H(m)|
\left\lfloor\frac Xm\right\rfloor\\
&\le
X\sum_{m\le X}\frac{|\mathcal H(m)|}{m}.
\end{aligned}
\tag{7}
\]

Hence the exact deterministic inequality

\[
\boxed{
L_{\mathcal H}(X)
\ge
\frac1X\sum_{N\le X}|\mathbf M(N)|.
}
\tag{8}
\]

Pintz's Theorems 2.1--2.2 give

\[
\log D_M(X)\sim\log Z(X),
\qquad
\frac{\log Z(X)}{\log X}\to\Theta,
\tag{9}
\]

where `Z` is his maximal zero term. Since `M(u)` is a step function, the discrete average on the right of (8) and `D_M(X)` differ only by an endpoint-sized term and have the same power exponent. Consequently

\[
\liminf_{X\to\infty}
\frac{\log(1+L_{\mathcal H}(X))}{\log X}
\ge\Theta.
\tag{10}
\]

For the opposite direction, `FD-046` gives, for every fixed `sigma>Theta`,

\[
|\mathcal H(n)|\ll_\sigma n^\sigma.
\tag{11}
\]

Therefore

\[
L_{\mathcal H}(X)
\ll_\sigma
\sum_{n\le X}n^{\sigma-1}
\ll_\sigma X^\sigma.
\tag{12}
\]

Letting `sigma` decrease to `Theta` proves (1).

This transfer is deliberately one-sided in absolute values: no cancellation in the inverse Mobius coefficients is used. The gain comes from summing the exact floor identity before estimating it, so the `1/d` inverse kernel and the `d`-fold quotient multiplicity cancel and leave precisely the logarithmic source weight `1/m`.

## 2. Every fixed power annulus carries the full source-mass exponent

Fix `0<lambda<1`. The upper bound in (12) also gives, for every `sigma>Theta`,

\[
L_{\mathcal H}(X^{1-\lambda})
\ll_\sigma
X^{(1-\lambda)\sigma}.
\tag{13}
\]

Because `Theta>=1/2`, one can choose `sigma>Theta` close enough to `Theta` that

\[
(1-\lambda)\sigma<\Theta.
\tag{14}
\]

Equation (1) then shows that the contribution below `X^(1-lambda)` is polynomially smaller than the full logarithmic source mass. Hence

\[
L_{\mathcal H}(X;\lambda)
=L_{\mathcal H}(X)-L_{\mathcal H}(X^{1-\lambda})
\]

has the same power exponent `Theta`, proving (2).

This is stronger in abundance than the maximal-order statement used in `FD-076`. `FD-076` says every fixed power annulus contains at least one frontier-scale source point and therefore a strict normalized record. Equation (2) says that the **total absolute physical source mass** in every such annulus already has the full frontier exponent.

## 3. Full annular mass forces full polynomial counting exponent

Fix `kappa>0`. We prove (3) by showing that for every arbitrarily small `delta>0`, the count `N_kappa(X)` is at least `X^(1-delta)` for all sufficiently large `X`.

Choose a fixed `lambda>0` and auxiliary exponents so small that

\[
\lambda<\kappa,
\qquad
\lambda+\epsilon_0+\epsilon_1<\delta,
\qquad
\lambda+\epsilon_0<\kappa.
\tag{15}
\]

By (2), for sufficiently large `X`,

\[
L_{\mathcal H}(X;\lambda)
\ge X^{\Theta-\epsilon_0}.
\tag{16}
\]

Since every `n` in this annulus satisfies `n>=X^(1-lambda)`, multiplying the logarithmic mass by the smallest possible `n` gives

\[
\sum_{X^{1-\lambda}<n\le X}|\mathcal H(n)|
\ge
X^{1-\lambda+\Theta-\epsilon_0}.
\tag{17}
\]

The contribution from values below the threshold `X^(Theta-kappa)` is at most

\[
X\cdot X^{\Theta-\kappa}
=X^{1+\Theta-\kappa},
\tag{18}
\]

which is polynomially smaller than (17) by the last condition in (15). Thus the points counted by `N_kappa(X)` carry at least a fixed fraction of the sum in (17).

On the other hand, `FD-046` gives for sufficiently large `X`

\[
|\mathcal H(n)|\ll_{\epsilon_1}X^{\Theta+\epsilon_1}
\qquad(n\le X).
\tag{19}
\]

Therefore

\[
N_\kappa(X)
\gg
X^{1-\lambda-\epsilon_0-\epsilon_1}
\ge X^{1-\delta}.
\tag{20}
\]

Since `delta>0` was arbitrary and trivially `N_kappa(X)<=X`, equation (3) follows.

The quantifiers matter. This is **not** a positive-density theorem and it does not say that one fixed proportion of all integers has frontier-size source. It says that no fixed polynomial sparsity exponent can contain all source values within a fixed polynomial tolerance of the zeta-zero frontier.

## 4. A fixed nonsquarefree row turns the abundance into causal occupation abundance

Fix `D` and any nonsquarefree `q>D`. At the causal horizon

\[
H=qn,
\]

the Jordan row `r=q` samples the source exactly at `n`:

\[
\left\lfloor\frac{qn}{q}\right\rfloor=n.
\tag{21}
\]

Because `q` is nonsquarefree, this row belongs to `U_(qn,D)`, and therefore

\[
\boxed{
U_{qn,D}
\ge
w(q)\mathcal H(n)^2.
}
\tag{22}
\]

For every `sigma>Theta`, `FD-046` gives the global energy envelope

\[
E_{H,D}\ll_{D,\sigma}H^{2\sigma}.
\tag{23}
\]

Take `kappa=eta/8` in (3), and choose

\[
\sigma=\Theta+\frac{\eta}{8}.
\tag{24}
\]

For every point counted by `N_(eta/8)(X)`, equations (22)--(24) yield

\[
\nu_{qn,D}
\ge
c_{D,q,\eta}
\frac{X^{2\Theta-\eta/4}}{X^{2\Theta+\eta/4}}
=
c_{D,q,\eta}X^{-\eta/2}.
\tag{25}
\]

Hence, for all sufficiently large `X`,

\[
\nu_{qn,D}\ge X^{-\eta}.
\tag{26}
\]

`FD-049` proves that the normalized Schur projective defect contains the whole nonsquarefree occupation,

\[
\varepsilon_{H,D}\ge\nu_{H,D},
\tag{27}
\]

so the same points satisfy `epsilon_(qn,D)>=X^(-eta)`. Since `N_(eta/8)(X)` has full polynomial counting exponent one, equation (4) follows.

The fixed row `q` is arbitrary apart from `q>D` and `mu(q)=0`. Thus the result does not rely specifically on the four-adic row. The four-adic choice remains the cheapest one for small heads, but the abundance phenomenon is an exact consequence of any fixed nonsquarefree causal dilation.

## 5. What this changes, and what it does not

The active frontier after `FD-076` was whether power-dense strict records could be upgraded to enough ordinary or logarithmic recurrence for their protected blocks to aggregate. Equations (1)--(4) bypass part of that question. Strict records themselves may remain very sparse, but **frontier-near physical source values do not**: for every fixed polynomial tolerance their counting function has exponent one. Likewise, at every prescribed polynomial occupation threshold `H^(-eta)`, causal nonsquarefree/projective protection occurs on a set of full counting exponent.

This is materially stronger than the generic pointwise estimate in `FD-049` when `Theta>1/2`. `FD-049` permits the all-horizon lower scale

\[
\nu_{H,D}\gtrsim H^{-(2\Theta-1)-o(1)}.
\]

The present result says that, on a full-counting-exponent family tied to frontier-near source values, the exponent can be made **arbitrarily close to zero**. Thus a false-RH source cannot hide all of its large physical values inside a polynomially sparse family of badly occupied causal horizons.

Three gaps remain explicit.

First, counting exponent one still allows zero ordinary density and zero logarithmic density. Second, (4) allows subpower occupation losses such as stretched exponentials in `log H`; it does not prove a fixed positive lower bound for `U/E`. Third, the theorem does not make the high values strict records, so the constant occupation mechanism of `FD-072` is not automatically inherited by all points counted here.

Accordingly, `CLUE-joint-nonsquarefree-jordan-energy-occupation` remains open. The sharper next target is no longer merely to manufacture more records. It is to upgrade the exponent-one abundance in (3)--(4) to either a positive density statement, a quantitatively stronger distributional moment, or a source-specific estimate that removes the residual subpower occupation loss.

## 6. Prior-art boundary

The external input is Pintz, *Oscillation of partial sums of the Möbius function and zeros of Riemann's zeta function*, arXiv `2608.24878v2` (2026), especially Theorems 2.1--2.2. Pintz proves both the average-order relation for `D_M` and the fixed-power-window maximal-order relation for `M`; `FD-076` used the latter, while the present finding uses the former through (8).

The zero-frontier upper envelope for `mathcal H` is already anchored through the classical Littlewood--Titchmarsh Mertens criterion in `FD-046`. A directed literature search around summatory functions with Dirichlet series `zeta(s+1)/zeta(s)`, the radical coefficient `mu(rad n)phi(rad n)/n`, and Mertens floor transforms did not locate the specific average-absolute transfer (8), the power-annulus consequence (2), or the Jordan-occupation abundance (4). No priority claim is made: the durable claim here is the explicit deduction from the cited average-order theorem and the exact Mathia floor/Jordan identities.

No new external theorem beyond sources already recorded in `SOURCES.md` is used.