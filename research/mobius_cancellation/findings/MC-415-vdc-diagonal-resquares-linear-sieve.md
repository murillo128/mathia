# MC-415 — First van der Corput diagonal re-squares the linear sieve

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The well-factorable upper-linear-sieve representation from `MC-409` escapes the *initial* quadratic Selberg/lcm coefficient because its source-character sum starts linearly:

\[
w(n)=\sum_{d\mid n}\lambda_d,
\qquad
S_\chi(N)=\sum_{n\le N}w(n)\chi(n).
\tag{1}
\]

However, the first ordinary additive van der Corput/Cauchy step necessarily introduces the zero-shift energy

\[
C_0(N):=\sum_{n\le N}|w(n)\chi(n)|^2.
\tag{2}
\]

That diagonal **re-squares the linear sieve weight exactly**. If

\[
C_\lambda(\ell)
:=
\sum_{[d,e]=\ell}\lambda_d\overline{\lambda_e},
\tag{3}
\]

then

\[
\boxed{
|w(n)|^2
=
\sum_{\ell\mid n}C_\lambda(\ell).
}
\tag{4}
\]

Thus the same lcm-fiber compression classified in `MC-398` reappears on the van der Corput diagonal even though the original majorant was linear rather than a Selberg square.

For a primitive Dirichlet character `chi` of conductor `q`, `|chi(n)|^2=1_(n,q)=1`, so `(2)` becomes

\[
\boxed{
C_0(N)
=
\sum_{\substack{\ell\le D^2\\(\ell,q)=1}}
C_\lambda(\ell)
\sum_{\substack{m\le N/\ell\\(m,q)=1}}1.
}
\tag{5}
\]

Consequently

\[
\boxed{
C_0(N)
=
N\frac{\varphi(q)}q
\sum_{\substack{d,e\le D\\(de,q)=1}}
\frac{\lambda_d\overline{\lambda_e}}{[d,e]}
+
O\!\left(
2^{\omega(q)}
\sum_{\ell\le D^2}|C_\lambda(\ell)|
\right).
}
\tag{6}
\]

The main diagonal is therefore the classical Selberg lcm quadratic form, restricted to divisors coprime to the source conductor. The source character contributes no oscillatory phase there.

There is a second exact form of the same obstruction. Extend

\[
a_n:=w(n)\chi(n)\mathbf 1_{1\le n\le N}
\tag{7}
\]

by zero to all integers and define

\[
C_h:=\sum_{n\in\mathbb Z}a_{n+h}\overline{a_n}.
\tag{8}
\]

For every integer `H>=1`, the triangular shift average satisfies

\[
\boxed{
\sum_{t\in\mathbb Z}
\left|\sum_{j=0}^{H-1}a_{t+j}\right|^2
=
\sum_{|h|<H}(H-|h|)C_h.
}
\tag{9}
\]

Since every `a_n` occurs in exactly `H` of the sliding windows,

\[
H\sum_n a_n
=
\sum_t\sum_{j=0}^{H-1}a_{t+j},
\tag{10}
\]

and Cauchy gives the standard finite van der Corput bound

\[
\boxed{
|S_\chi(N)|^2
\le
\frac{N+H-1}{H^2}
\sum_{|h|<H}(H-|h|)C_h.
}
\tag{11}
\]

The right-hand side is a positive Fejér/sliding-window energy and contains the diagonal term `H C_0`. Therefore **jointly averaging the shifted correlations with the standard positive triangular kernel does not preserve the linear-sieve escape on the diagonal**: the diagonal has already returned to the lcm quadratic closure before any estimate for the incomplete translated off-diagonal family is used.

This does **not** kill the `MC-409` route. The off-diagonal `C_h`, `h!=0`, still contains the genuine incomplete translated correlations isolated by `MC-413`, and `MC-414` shows that their remaining possible leverage lies in the divisor-dependent sampling geometry/weights. The exact consequence is narrower:

> any continuation based on ordinary positive van der Corput shift averaging has two independent obligations. It must control the re-quadratized lcm diagonal `(5)`--`(6)`, and it must obtain an off-diagonal gain before the well-factorable/divisor geometry is erased. The first-moment upper-sieve estimate used to build the prime frame does not by itself certify the second-moment diagonal required by differencing.

No improved character-sum estimate, source-depth exponent, Mertens bound, or RH consequence follows.

## 1. Exact lcm return on the zero shift

From `(1)`,

\[
\begin{aligned}
|w(n)|^2
&=
\left(\sum_{d\mid n}\lambda_d\right)
\left(\sum_{e\mid n}\overline{\lambda_e}\right)\\
&=
\sum_{d,e}\lambda_d\overline{\lambda_e}
\mathbf 1_{d\mid n}\mathbf 1_{e\mid n}\\
&=
\sum_{d,e}\lambda_d\overline{\lambda_e}
\mathbf 1_{[d,e]\mid n}.
\end{aligned}
\tag{12}
\]

Grouping by `ell=[d,e]` gives `(4)` exactly. This is precisely the sufficient-statistic mechanism of `MC-398`: once both divisibility conditions hit the same integer, the pair enters the arithmetic object only through its least common multiple.

Now use primitivity only to identify the support of the character norm:

\[
|\chi(n)|^2=\mathbf 1_{(n,q)=1}.
\tag{13}
\]

Substitute `(4)` into `(2)` and write `n=ell m`. If `(ell,q)>1`, the term is zero. If `(ell,q)=1`, the remaining condition is `(m,q)=1`, giving `(5)`.

For `X>=0`, inclusion-exclusion gives

\[
\sum_{\substack{m\le X\\(m,q)=1}}1
=
\frac{\varphi(q)}q X+O(2^{\omega(q)}).
\tag{14}
\]

Using `(14)` termwise in `(5)` yields

\[
C_0(N)
=
N\frac{\varphi(q)}q
\sum_{\substack{\ell\le D^2\\(\ell,q)=1}}
\frac{C_\lambda(\ell)}\ell
+
O\!\left(
2^{\omega(q)}\sum_\ell|C_\lambda(\ell)|
\right).
\tag{15}
\]

Finally,

\[
\sum_{\substack{\ell\\(\ell,q)=1}}
\frac{C_\lambda(\ell)}\ell
=
\sum_{\substack{d,e\\(de,q)=1}}
\frac{\lambda_d\overline{\lambda_e}}{[d,e]},
\tag{16}
\]

which proves `(6)`.

The form in `(16)` is positive semidefinite in the only sense needed here: `(2)` is nonnegative for every `N`, and its normalized main term is the standard Selberg quadratic kernel. No cancellation from `chi` is available on this diagonal; `chi` has collapsed to coprimality with `q`.

## 2. The triangular shift family is exactly a Fejér energy

Expand the left side of `(9)`:

\[
\begin{aligned}
\sum_t
\left|\sum_{j=0}^{H-1}a_{t+j}\right|^2
&=
\sum_t\sum_{j,k=0}^{H-1}
 a_{t+j}\overline{a_{t+k}}.
\end{aligned}
\tag{17}
\]

For fixed `h=j-k`, there are exactly `H-|h|` pairs `(j,k)` with that difference. Translating the `t`-sum then gives `(9)`.

Equivalently, if

\[
A(\theta)=\sum_n a_n e(n\theta),
\qquad
D_H(\theta)=\sum_{j=0}^{H-1}e(j\theta),
\tag{18}
\]

then Parseval gives

\[
\boxed{
\sum_{|h|<H}(H-|h|)C_h
=
\int_0^1 |A(\theta)|^2|D_H(\theta)|^2\,d\theta.
}
\tag{19}
\]

Thus the standard collective shift geometry is a positive Fourier multiplier. It does not create a second independent source phase by summing `h`; this is consistent with the endpoint-separable kernel and flat two-dimensional Gauss spectrum proved in `MC-414`.

The important new point relative to `MC-414` is the **cost of the diagonal after inserting the actual linear-sieve weight**. The same operation that creates translated off-diagonal phases also replaces the first-moment object `w` by the second-moment object `|w|^2` at `h=0`, and `(12)` forces that second moment into lcm fibers.

## 3. Why the prime-frame first moment is not enough

`MC-409` checked that the upper linear sieve preserves the prime-frame architecture through two facts:

\[
w(n)\ge0,
\qquad
\sum_{n\le N}w(n)\ll_s \frac{N}{\log z}+D.
\tag{20}
\]

Those facts concern the **first moment**. Van der Corput requires the second moment `(2)`.

For an arbitrary nonnegative weight, a first-moment upper bound gives no comparable upper bound for the second moment: spikes can preserve `sum w` while making `sum w^2` much larger. The divisor-sum structure of the actual Iwaniec/linear-sieve coefficients may well control `(6)` efficiently, but that is an additional theorem/estimate, not a consequence of `(20)` alone.

A crude bound illustrates why this is a quantitative question rather than an automatic fatal obstruction. If the chosen sieve coefficients satisfy `|lambda_d|<=1`, then

\[
0\le w(n)\le \tau(n)
\tag{21}
\]

for the upper-bound weight, hence standard divisor-moment estimates give only polylogarithmic/subpower growth for the average second moment. Such a loss may be harmless for an exponent-level source-depth argument. But the branch cannot simply reuse the `N/log z` first-moment diagonal from `MC-409` after differencing without proving the relevant second-moment bound for the exact coefficient family.

This separates two questions that had been bundled together:

1. whether a positive well-factorable **linear** majorant can replace the original Selberg square in the prime-frame inner product — `MC-409` says yes at representation/first-moment level;
2. whether a **quadratic differencing method** can exploit that linear representation without paying an uncontrolled lcm quadratic diagonal — `(4)`--`(16)` show that the lcm form returns exactly and must be budgeted separately.

## 4. Prior-art and novelty boundary

No novelty is claimed for either mechanism in isolation.

The van der Corput correlation inequality and its Hilbert-space variants are classical consequences of Cauchy--Schwarz. A modern reference is N. Edeko, H. Kreidler and R. Nagel, *A dynamical proof of the van der Corput inequality*, Dynamical Systems **37** (2022), 1805--1825, DOI `10.1080/14689367.2022.2100244`, arXiv:`2106.11835`. The finite sliding-window identity `(9)` and the inequality `(11)` are derived directly here, so no theorem-strength claim depends on that reference.

The lcm quadratic form in `(16)` is standard Selberg-sieve structure. `MC-398` already audited the exact compression `1_(d|n)1_(e|n)=1_([d,e]|n)` against classical Selberg-sieve presentations. Standard formulations optimize quadratic forms of the shape

\[
\sum_{d,e}\rho_d\rho_e\,g([d,e]),
\tag{22}
\]

and the present `(16)` is precisely the counting-kernel specialization `g(ell)=1/ell` with a source-coprimality restriction.

A targeted literature check on 20 September 2026 found the two ingredients as standard prior art but no reason to treat their combination here as a new analytic theorem. The durable Mathia contribution is the frontier classification: the `MC-409` representation avoids the old lcm closure only **before** the first quadratic differencing/energy step; ordinary van der Corput restores that closure on its diagonal.

## Boundaries and falsification tests

- **This is not a collapse of the off-diagonal.** For `h!=0`, `MC-413` still leaves genuinely incomplete translated character correlations. The present finding concerns the unavoidable zero-shift/energy term and positive joint shift averaging.
- **The lcm return need not be quantitatively fatal.** A sharp second-moment theorem for the actual Iwaniec upper-sieve weight could keep `(6)` on an acceptable scale. This finding proves the required object, not a bad asymptotic for it.
- **Well-factorability is not claimed to disappear everywhere.** The coefficient convolution can still be exploited before absolute values in the off-diagonal. What disappears on the diagonal is the idea that the original linear representation by itself avoids quadratic lcm geometry.
- **Positive triangular averaging is load-bearing.** A signed/oscillatory shift weight or a modulus-factorized `A`-process may retain different information. Equation `(9)` classifies the standard Fejér kernel, not every possible shift operator.
- **No source oscillation survives in `(6)`.** The primitive character enters only through `(ell,q)=1` and the coprime density `phi(q)/q`; any claimed diagonal source saving from character phase is therefore spurious.
- **The first-moment sieve estimate cannot be substituted for `(2)`.** Any continuation that quotes only `sum w << N/log z` after applying Cauchy/van der Corput has omitted a new quadratic cost.
- **No RH-scale input is used.** All identities are finite divisor algebra, coprime counting, Cauchy--Schwarz, and Parseval.

## Consequence for the research line

The `MC-409` escape remains live but is now narrower. `MC-413`--`MC-414` locate the potentially useful off-diagonal information in incomplete, divisor-dependent sampling geometry. The present finding shows that the ordinary van der Corput mechanism simultaneously recreates the old lcm quadratic structure on the diagonal.

The next viable calculation must therefore carry **both budgets** at once for a concrete well-factorable upper-sieve component:

\[
\text{diagonal cost}
\quad\leftrightarrow\quad
\sum_{d,e}\frac{\lambda_d\overline{\lambda_e}}{[d,e]},
\tag{23}
\]

and the incomplete shifted off-diagonal from `MC-413`--`MC-414`. A useful source-depth improvement must show that the off-diagonal theorem wins more than any new second-moment/lcm cost loses. If the proof handles the diagonal by silently importing the old first-moment `N/log z` scale, the claimed gain is not yet established.