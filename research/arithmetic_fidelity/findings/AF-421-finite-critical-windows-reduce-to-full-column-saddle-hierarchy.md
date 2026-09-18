# AF-421 — Finite critical windows reduce to a full-column saddle hierarchy

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DOUBLE-SCALING` · `DERIVATIVE-SHIFT` · `SIGNED-RESUMMATION` · `FULL-COLUMN-SADDLE` · `SCHUR-PIERI` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-417--AF-420 with the normalized exceptional-`1` sector

\[
S_n^{(s)}(a)
=
\sum_{\ell(\lambda)\le n}
(-1)^{|\lambda|}
\left(\frac{a}{n^2}\right)^{|\lambda|}
s_\lambda(1^n)^2
R_{n,\lambda}^{(s)},
\qquad
a>0,
\tag{1}
\]

where

\[
R_{n,\lambda}^{(s)}
=
\prod_{i=1}^{n}
\left(\frac{k_i}{i}\right)^{s-1}
\frac{\zeta(2k_i)}{\zeta(2i)}
\left(\frac{2k_i-1}{2i-1}\right)^2,
\qquad
k_i=i+\lambda_{n+1-i}.
\tag{2}
\]

Let `s_n` be nonnegative integers such that

\[
\frac{s_n}{n}\longrightarrow 2,
\tag{3}
\]

and suppose the AF-420 effective coordinate has a finite positive limit

\[
b_n
:=
a\,n^{s_n/n-2}
\longrightarrow
b\in(0,\infty).
\tag{4}
\]

For `r>=0`, define the exact magnitude of the rectangular contribution `lambda=(r^n)` by `C_{n,0}=1` and

\[
C_{n,r}
=
\left(\frac{a}{n^2}\right)^{rn}
\binom{n+r}{r}^{s_n-1}
\frac{\prod_{j=n+1}^{n+r}\zeta(2j)}
     {\prod_{j=1}^{r}\zeta(2j)}
\left[
\frac{\prod_{j=n+1}^{n+r}(2j-1)}
     {\prod_{j=1}^{r}(2j-1)}
\right]^2.
\tag{5}
\]

Then, for every fixed `r`,

\[
C_{n,r}^{1/n}
\longrightarrow
L_r(b)
:=
\frac{b^r}{(r!)^2}.
\tag{6}
\]

Let

\[
\mathcal M(b)
=
\operatorname*{arg\,max}_{r\ge0}L_r(b).
\tag{7}
\]

Because

\[
\frac{L_{r+1}(b)}{L_r(b)}
=
\frac{b}{(r+1)^2},
\tag{8}
\]

the maximizer set is explicit:

\[
\mathcal M(b)
=
\begin{cases}
\{\lfloor\sqrt b\rfloor\}, & b\notin\{1,4,9,\ldots\},\\[4pt]
\{m-1,m\}, & b=m^2,\quad m\ge1.
\end{cases}
\tag{9}
\]

Put

\[
E(a)=e^{-a e^2}.
\tag{10}
\]

Then the **complete signed partition sum** has the saddle reduction

\[
\boxed{
S_n^{(s_n)}(a)
=
E(a)
\sum_{r\in\mathcal M(b)}
(-1)^{rn} C_{n,r}
+
o\!\left(
\sum_{r\in\mathcal M(b)} C_{n,r}
\right).
}
\tag{11}
\]

Thus the signed problem left open by AF-420 is not governed by arbitrary cancellation among the whole partition family. In every finite critical window, all exponentially leading mass is forced into one full-column rectangle packet, except at the discrete transition values

\[
\boxed{b=1,4,9,\ldots}
\tag{12}
\]

where two adjacent full-column packets have the same exponential rate.

In particular, if `b>1` is not a perfect square and

\[
r_*=\lfloor\sqrt b\rfloor,
\]

then

\[
\boxed{
\frac{
S_n^{(s_n)}(a)
}{
(-1)^{r_*n}C_{n,r_*}
}
\longrightarrow
e^{-a e^2}.
}
\tag{13}
\]

Since `L_{r_*}(b)>1`, the normalized sector grows exponentially in magnitude. Therefore the fixed-partition candidate `e^{-a e^2}` does **not** survive signed resummation anywhere in the non-square superthreshold finite-`tau` regime.

At a square transition `b=m^2`, `(11)` becomes

\[
S_n^{(s_n)}(a)
=
E(a)(-1)^{(m-1)n}C_{n,m-1}
\left[
1+(-1)^n F_{n,m}
\right]
+
o(C_{n,m-1}+C_{n,m}),
\tag{14}
\]

where the exact adjacent-packet ratio is

\[
\boxed{
F_{n,m}
:=
\frac{C_{n,m}}{C_{n,m-1}}
=
\left(\frac{a}{n^2}\right)^n
\left(\frac{n+m}{m}\right)^{s_n-1}
\frac{\zeta(2(n+m))}{\zeta(2m)}
\left(\frac{2(n+m)-1}{2m-1}\right)^2.
}
\tag{15}
\]

Equation `(15)` isolates the only remaining finite-window cancellation gate: on odd `n`, adjacent leading packets have opposite signs, and a further asymptotic is needed only when `F_{n,m}` is close enough to `1` for their leading terms to cancel.

The first transition `b=1` can be sharpened completely for the exact critical sequence. When

\[
s_n=2n,\qquad a=1,
\tag{16}
\]

AF-420's full-height-column magnitude satisfies

\[
C_{n,1}
\sim
\frac{24e^2}{\pi^2}n,
\tag{17}
\]

so `(11)` gives

\[
\boxed{
\frac{(-1)^n}{n}
S_n^{(2n)}(1)
\longrightarrow
\frac{24e^{\,2-e^2}}{\pi^2}.
}
\tag{18}
\]

Hence the exact boundary `c=2pi` does not merely defeat absolute domination: the complete signed exceptional-`1` sector itself diverges linearly with parity-alternating sign.

## 1. Exact decomposition by the number of full-height columns

Every partition `lambda` with `ell(lambda)<=n` has a unique decomposition

\[
\lambda=(r^n)+\mu,
\qquad
r=\lambda_n,
\qquad
\mu_n=0.
\tag{19}
\]

Adding the rectangle `(r^n)` is the usual determinant twist,

\[
s_{\mu+(r^n)}(x_1,\ldots,x_n)
=
(x_1\cdots x_n)^r s_\mu(x_1,\ldots,x_n),
\tag{20}
\]

so in particular

\[
s_{\mu+(r^n)}(1^n)=s_\mu(1^n).
\tag{21}
\]

Write

\[
\delta_i=\mu_{n+1-i}.
\]

Relative to the rectangle `(r^n)`, the exact residual perturbation is

\[
\mathcal R_{n,r,\mu}^{(s)}
=
\prod_{i=1}^{n}
\left(
\frac{i+r+\delta_i}{i+r}
\right)^{s-1}
\frac{\zeta(2(i+r+\delta_i))}
     {\zeta(2(i+r))}
\left(
\frac{2(i+r+\delta_i)-1}
     {2(i+r)-1}
\right)^2.
\tag{22}
\]

Define the residual packet

\[
G_{n,r}
=
\sum_{\mu_n=0}
(-1)^{|\mu|}
\left(\frac{a}{n^2}\right)^{|\mu|}
s_\mu(1^n)^2
\mathcal R_{n,r,\mu}^{(s_n)}.
\tag{23}
\]

Then `(19)`--`(23)` give the exact identity

\[
\boxed{
S_n^{(s_n)}(a)
=
\sum_{r\ge0}
(-1)^{rn}C_{n,r}G_{n,r}.
}
\tag{24}
\]

The zeta and odd-distance products in `(5)` follow by telescoping the rectangle ratios. In particular the rectangle magnitudes factor column-by-column:

\[
C_{n,r}
=
\prod_{m=1}^{r}F_{n,m},
\tag{25}
\]

with `F_{n,m}` exactly as in `(15)`.

For fixed `m`, `(4)` and `(15)` imply

\[
F_{n,m}^{1/n}\longrightarrow\frac{b}{m^2},
\tag{26}
\]

which proves `(6)` and the discrete saddle rule `(8)`--`(9)`.

## 2. Each leading rectangle carries the same Schur-Cauchy packet

Fix `r`. For a fixed residual partition `mu` of degree `d`, only indices `i=n+O_mu(1)` have `delta_i>0`. Hence

\[
\log
\prod_{i=1}^{n}
\frac{i+r+\delta_i}{i+r}
=
\frac{d}{n}+O_\mu(n^{-2}).
\tag{27}
\]

Using `(3)`,

\[
\prod_{i=1}^{n}
\left(
\frac{i+r+\delta_i}{i+r}
\right)^{s_n-1}
\longrightarrow e^{2d}.
\tag{28}
\]

The zeta and odd-distance ratios in `(22)` tend to one, while the hook-content formula gives

\[
\frac{s_\mu(1^n)}{n^d}
\longrightarrow
\frac1{H_\mu}.
\tag{29}
\]

Therefore every fixed residual partition has the limit

\[
(-1)^d
\left(\frac{a}{n^2}\right)^d
s_\mu(1^n)^2
\mathcal R_{n,r,\mu}^{(s_n)}
\longrightarrow
\frac{(-a e^2)^d}{H_\mu^2}.
\tag{30}
\]

Summing over partitions of fixed degree and using

\[
\sum_{\mu\vdash d}\frac1{H_\mu^2}=\frac1{d!},
\tag{31}
\]

gives the degree-`d` coefficient of `E(a)`.

The remaining issue is again uniformity over unbounded residual partitions. The AF-420 column argument adapts with one important improvement: `mu_n=0`, so every residual tall column has height at most `n-1`.

Define the shifted column product

\[
P_{n,r,\mu}
=
\prod_{i=1}^{n}
\frac{i+r+\delta_i}{i+r}
=
\prod_{m\ge1}
\frac{n+r+m}{n-h_m+r+m},
\qquad
h_m=\mu'_m.
\tag{32}
\]

The crude AF-419 estimate and the sharper AF-420 odd-distance comparison remain valid after the shift, because increasing `r` only decreases the rational distortion. Thus for suitable absolute constants,

\[
\mathcal R_{n,r,\mu}^{(s_n)}
\le
9^{|\mu|}P_{n,r,\mu}^{s_n-1},
\tag{33}
\]

and also

\[
\mathcal R_{n,r,\mu}^{(s_n)}
\le
e^2n^2 P_{n,r,\mu}^{s_n+1}.
\tag{34}
\]

Choose `eta` with `1/2<eta<1`. If all columns satisfy `h_m<=eta n`, then `(32)` gives

\[
P_{n,r,\mu}
\le
\exp\!\left(
\frac{|\mu|}{(1-\eta)n}
\right),
\tag{35}
\]

uniformly in `r`. Since `s_n/n->2`, `(33)` turns `(35)` into a bound `C_eta^{|mu|}`. The positive Schur Cauchy identity therefore gives a degree tail tending to zero uniformly in `n` and `r`.

For a residual tall column write

\[
h=n-j,\qquad j\ge1.
\]

After the same Pieri split as AF-420, its scalar factor is

\[
B_{n,r,m}(n-j;a)
=
\left(\frac{a}{n^2}\right)^{n-j}
\binom nj^2
\left(
\frac{n+r+m}{j+r+m}
\right)^{s_n+1}.
\tag{36}
\]

For fixed `r,m,j`,

\[
B_{n,r,m}(n-j;a)^{1/n}
\longrightarrow
\frac{b}{(r+m+j)^2}.
\tag{37}
\]

If `j->infinity` while `j<(1-eta)n`, the same two-range estimate as AF-420 equations `(35)`--`(37)` makes `(36)` superexponentially smaller than every fixed-`j` candidate. Thus, whenever

\[
b<(r+2)^2,
\tag{38}
\]

the complete residual tall-column sector vanishes absolutely, because the largest possible fixed-defect factor is the first column with `m=1,j=1`.

Every `r` in the maximizing set `M(b)` satisfies `(38)`. Therefore

\[
\boxed{
G_{n,r}\longrightarrow E(a)
\qquad
(r\in\mathcal M(b)).
}
\tag{39}
\]

The same estimates, without taking a limit, give a uniform absolute bound for the residual packet after any fixed number of full columns. They also give the bounds needed below when the full-column count varies.

## 3. A tall-column Laplace principle leaves only the maximizing rectangles

It remains to show that partitions outside the maximizing packets are exponentially smaller.

Use the AF-420 tall-column decomposition before replacing all tall-column factors by the first one. If the `m`-th tall column has height

\[
h_m=n-j_m,
\qquad
j_m\ge0,
\]

its scalar factor is

\[
B_{n,m}(n-j_m;a)
=
\left(\frac{a}{n^2}\right)^{n-j_m}
\binom n{j_m}^2
\left(
\frac{n+m}{j_m+m}
\right)^{s_n+1}.
\tag{40}
\]

For every fixed `m,j`,

\[
B_{n,m}(n-j;a)^{1/n}
\longrightarrow
\frac{b}{(m+j)^2}.
\tag{41}
\]

For `j->infinity`, uniformly over the tall range, the nth root tends to zero: for `j=o(n)` the denominator `(m+j)^{s_n+1}` dominates the subexponential binomial factor, while for `j` proportional to `n` the factor `n^{-2h}` gives the AF-420 superexponential estimate.

Consequently a fixed tall profile with `q` columns has exponential rate at most

\[
\prod_{m=1}^{q}
\frac{b}{(m+j_m)^2}
\le
\frac{b^q}{(q!)^2}
=
L_q(b),
\tag{42}
\]

with equality only when every `j_m=0`, i.e. when all tall columns are genuinely full-height.

The no-tall residual has only a bounded Schur-Cauchy normalization on the nth-root scale. The number of height profiles with any fixed `q` is polynomial in `n`, and for large `q` the factors `b/m^2` are uniformly below one. Hence growing `q` cannot create a new exponential saddle.

Because `L_q(b)->0` superfactorially and `(8)` is unimodal, there is a strict exponential gap between the profiles indexed by `M(b)` and every other tall profile. Combining this gap with `(39)` and the exact decomposition `(24)` gives `(11)`.

This is the step that AF-420 could not take after collapsing every tall column to the common majorant `B_{n,1}`. Retaining the **column index `m` together with the height defect `j_m`** exposes the full signed saddle hierarchy.

## 4. Square transitions are the only finite-window cancellation interfaces

When `b` is not a perfect square, `(8)` gives a unique maximizing rectangle. Equation `(13)` follows immediately from `(11)`.

When `b=m^2`, two adjacent rectangles have the same nth-root rate:

\[
L_{m-1}(m^2)=L_m(m^2).
\tag{43}
\]

All other partition profiles remain exponentially lower. Therefore the complete signed problem reduces to the explicit two-packet expression `(14)`.

The ratio `F_{n,m}` in `(15)` is not an arbitrary new observable. It is exactly the incremental cost of adding the `m`-th full-height column. Its nth root tends to one at the square transition:

\[
F_{n,m}^{1/n}\to1.
\tag{44}
\]

Thus only subexponential information beyond `b_n->m^2` can decide which adjacent packet dominates.

Parity matters. For even `n`, the two signs in `(14)` agree, so leading cancellation is impossible. For odd `n`, they oppose, and cancellation can occur only if the finer scale drives

\[
F_{n,m}\to1
\tag{45}
\]

with enough precision to cancel the next asymptotic order.

For the first square `b=1`, `m=1` and `C_{n,0}=1`. On the exact sequence `(16)`, AF-420 gives `(17)`, so the second packet dominates polynomially rather than cancelling. Substitution into `(14)` proves `(18)`.

More generally at `b=1`, `(15)` with `m=1` gives

\[
C_{n,1}
\sim
\frac{24e^2}{\pi^2}
\,n\,b_n^n.
\tag{46}
\]

Hence the next boundary coordinate is

\[
\Gamma_n
=
n\,b_n^n,
\qquad
\log\Gamma_n
=
\log n+n\log b_n.
\tag{47}
\]

Inside the `b_n->1` layer:

- if `Gamma_n->0`, the fixed-partition candidate survives;
- if `Gamma_n->gamma in (0,infinity)`, the two parity subsequences retain a finite packet correction of size `(24e^2/pi^2) gamma E(a)`;
- if `Gamma_n->infinity`, the one-full-column packet dominates and the sector has parity-controlled divergence.

Thus the nth-root coordinate `b_n` is itself compressed at the square boundary; `(47)` is the next scale required to recover the signed behavior.

## 5. Arithmetic-fidelity interpretation

AF-417 showed that bounded partitions retain only `s_n/n`. AF-418 and AF-420 showed that full-height partitions retain the finer coordinate `b_n`. The present result shows that even after `b_n` is retained, the signed sum is organized by another discrete piece of structure: **how many full-height columns survive**.

The transformation therefore has a hierarchy of retained information:

\[
\frac{s_n}{n}
\quad\rightsquigarrow\quad
b_n=a\,n^{s_n/n-2}
\quad\rightsquigarrow\quad
r=\text{full-column count}
\quad\rightsquigarrow\quad
F_{n,m}\text{ at square ties}.
\]

This is not merely a larger error estimate. Collapsing all tall partitions into one absolute majorant erases the column index and therefore erases the discrete saddle structure. Keeping the relational labels `(m,j_m)` turns the previously unresolved signed cancellation question into a finite saddle-selection problem.

No rational-prime discriminator appears here and no RH consequence follows. The result is a structural example of Arithmetic Fidelity's main theme: an asymptotic compression can be valid away from transition fibers while losing exactly the finer coordinates needed on those fibers.

## Prior-art and novelty audit

The determinant-twist identity `(20)`, hook-content asymptotics, Pieri rule, and Schur Cauchy identity are classical symmetric-function and `GL_n` representation theory; a standard source is I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford University Press (1995), Chapter I.

A. Okounkov, **“Infinite wedge and random partitions,”** *Selecta Mathematica (N.S.)* 7(1), 57--81 (2001), arXiv:`math/9907127`, and A. Okounkov--N. Reshetikhin, **“Correlation function of Schur process with application to local geometry of a random 3-dimensional Young diagram,”** *J. Amer. Math. Soc.* 16(3), 581--603 (2003), DOI:`10.1090/S0894-0347-03-00425-9`, are established prior art for Schur-measure/process normalization and asymptotic partition geometry.

K. Dilcher and L. Jiu, **“Hankel Determinants of sequences related to Bernoulli and Euler Polynomials,”** *International Journal of Number Theory* 18(2), 331--359 (2022), DOI:`10.1142/S179304212250021X`, and **“Hankel Determinants of shifted sequences of Bernoulli and Euler numbers,”** *Contributions to Discrete Mathematics* 18(2) (2023), DOI:`10.55016/ojs/cdm.v18i2.73995`, show that Bernoulli/Euler Hankel determinants and shifted Hankel sequences have substantial classical/modern prior art.

A targeted search across Schur measures/processes, rectangular/full-column partition asymptotics, and Bernoulli/Euler Hankel determinants did not locate the specific Euler-log derivative-Hankel weight `(2)`, the packet factorization `(24)`, or the square-transition saddle rule `(9)`--`(15)`. No novelty is claimed for any of the classical Schur or Hankel ingredients; the durable contribution is their exact specialization to the AF-417 varying-derivative sector and the resulting signed phase reduction.

## Boundaries and falsification checks

- The theorem concerns only the exceptional-`1` Cauchy--Binet sector `S_n^{(s_n)}(a)`. AF-416's omitted-`1` and one-/zero-singular-block sectors have not yet been re-audited for growing derivative shift.
- The finite-window assumption is `s_n/n->2` with `b_n->b in (0,infinity)`. Genuinely supercritical ratios `s_n/n->sigma>2` remain outside the theorem.
- At square transitions `b=m^2`, `(11)` is a two-packet reduction, not a claim that the two packets fail to cancel. Odd-`n` fine tuning with `F_{n,m}` near one remains a live boundary problem.
- The use of the AF-420 tall-column majorant is only for exclusion of nonleading profiles. The leading rectangle amplitudes and packet ratios are exact.
- Polynomial or subexponential prefactors are irrelevant away from square ties but become decisive at the ties; they must not be discarded there.
- The exact `b=1`, `s_n=2n`, `a=1` corollary uses AF-420's audited asymptotic for `C_{n,1}`. It does not automatically extend to arbitrary sequences with `b_n->1`.
- No statement about total positivity, rational-prime fidelity, zeta zeros, or RH follows.

## Consequence for the research line

The accepted `CLUE-linear-derivative-shift-full-tail` can now be narrowed sharply. Inside every finite-`tau` critical window, the complete signed exceptional-`1` sector is controlled by a discrete full-column saddle. Non-square superthreshold values do not admit a hidden global cancellation back to the fixed-partition exponential: one rectangle packet dominates exponentially.

The only unresolved finite-window cancellation interfaces are the square values `b=m^2`, where two adjacent packets tie on the nth-root scale. Their exact ratio is already isolated by `(15)`, so the next finite-window task is a finer asymptotic of `F_{n,m}` on odd `n` when it approaches one. The exact first boundary `b=1`, `s_n=2n`, `a=1` is closed by `(18)`.

After the square-transition problem is exhausted, the separate genuinely supercritical regime `s_n/n>2` remains.
