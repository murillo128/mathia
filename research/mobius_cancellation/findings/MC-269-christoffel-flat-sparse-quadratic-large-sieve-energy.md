# MC-269 — The Christoffel detector is a flat sparse quadratic large-sieve energy

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the shell notation of `MC-264`–`MC-268`. Put

\[
\mathcal B_m=\{S\subseteq\mathcal P_y:|S|\le m\},
\qquad
Z=|\mathcal B_m|=Z_m(k_y)=\sum_{s=0}^m\binom{k_y}{s},
\]

and for `S\in\mathcal B_m` write

\[
q_S=\prod_{p\in S}p.
\]

For a shell subset `T\in\binom{\mathcal R_y}{t}`, define

\[
\chi_T(q_S)
=\prod_{r\in T}\left(\frac{q_S}{r}\right)
=\prod_{p\in S}\sigma_p(T).
\]

The Christoffel polynomial of `MC-268` has the exact Walsh form

\[
\boxed{
P_m\!\left(b_y(T);k_y\right)
=\frac1Z\sum_{S\in\mathcal B_m}\chi_T(q_S).
}
\tag{1}
\]

Consequently its endpoint energy is exactly

\[
\boxed{
\mathcal E_{m,y}(t)
=\frac1{Z^2}
\sum_{|T|=t}
\left|\sum_{S\in\mathcal B_m}\chi_T(q_S)\right|^2.
}
\tag{2}
\]

Thus the candidate estimate isolated in `MC-268`,

\[
\mathcal E_{m,y}(t)
\le
L_y\frac{\binom{N_y}{t}}{Z},
\tag{3}
\]

is **equivalent** to the flat-coefficient sparse-family quadratic large-sieve estimate

\[
\boxed{
\sum_{|T|=t}
\left|\sum_{S\in\mathcal B_m}\chi_T(q_S)\right|^2
\le
L_y\binom{N_y}{t}Z.
}
\tag{4}
\]

The literal diagonal `S=U` in the expansion of `(4)` is exactly

\[
\binom{N_y}{t}Z.
\tag{5}
\]

So `(4)` asks for control at a loss `L_y` times the natural diagonal of one very explicit rectangular quadratic-character matrix: rows are the fixed-weight shell products

\[
q_T=\prod_{r\in T}r,
\qquad |T|=t,
\]

and columns are square-free products of at most `m` lower primes. The high-order endpoint problem has therefore become a **second-moment problem after the correct nonlinear lift**. No high-moment coefficient multiplicities remain in `(4)`; every source column has coefficient one.

There is a second exact consequence. The Krawtchouk coefficients left implicit in `MC-268` are nonnegative Hamming-ball self-convolution coefficients. For a fixed `V\subseteq\mathcal P_y`, `|V|=d`, define

\[
a_{m,k}(d)
=
\#\{S\subseteq[k]:|S|\le m,\ |S\triangle V|\le m\}.
\tag{6}
\]

Equivalently, `a_{m,k}(d)` is the intersection size of a Hamming ball of radius `m` with its translate by a vector of weight `d`. Then

\[
\boxed{
P_m(b;k)^2
=
\sum_{d=0}^{2m}
\frac{a_{m,k}(d)}{Z_m(k)^2}
K_d(b;k).
}
\tag{7}
\]

In particular the coefficients in `MC-268` are

\[
\boxed{
\gamma_{m,d}(k)=\frac{a_{m,k}(d)}{Z_m(k)^2}\ge0.
}
\tag{8}
\]

The intersection numbers are completely explicit:

\[
\boxed{
a_{m,k}(d)
=
\sum_{j=0}^{d}\binom dj
\sum_{\ell=0}^{m-\max(j,d-j)}\binom{k-d}{\ell},
}
\tag{9}
\]

where an inner sum with negative upper limit is zero.

Define

\[
w_{m,k}(d)
=\binom kd\frac{a_{m,k}(d)}{Z_m(k)^2}.
\tag{10}
\]

Then `w_{m,k}` is a probability distribution: it is exactly the law of

\[
D=|S\triangle U|
\]

for independent uniformly chosen `S,U\in\mathcal B_m`. With

\[
h_{d,y}(t)
=
\frac{H_{d,y}(t)}{\binom{k_y}{d}\binom{N_y}{t}},
\]

equations `(7)` and `MC-267` give

\[
\boxed{
\frac{\mathcal E_{m,y}(t)}{\binom{N_y}{t}}
=
\sum_{d=0}^{2m}w_{m,k_y}(d)h_{d,y}(t)
=
\frac1Z+
\sum_{d=1}^{2m}w_{m,k_y}(d)h_{d,y}(t).
}
\tag{11}
\]

Here `h_{0,y}(t)=1` and

\[
w_{m,k}(0)=\frac1Z.
\tag{12}
\]

Equation `(11)` exposes a sharp obstruction to a seemingly natural proof strategy. Suppose one tries to prove `(3)` by bounding every nonzero source-support layer separately,

\[
|h_{d,y}(t)|\le\eta_d,
\]

and then taking absolute values in `(11)`. Such a proof must satisfy

\[
\sum_{d\ge1}w_{m,k_y}(d)\eta_d
\le\frac{L_y-1}{Z}.
\tag{13}
\]

The required precision is much stronger than the probability weights initially suggest. For every `1\le j\le m`, the boundary pairs `|S|=|U|=m` with `|S\triangle U|=2j` give the exact lower bound

\[
a_{m,k}(2j)
\ge
\binom{2j}{j}\binom{k-2j}{m-j},
\]

and therefore

\[
\boxed{
\frac{w_{m,k}(2j)}{w_{m,k}(0)}
\ge
\frac{\binom{k}{m}}{Z_m(k)}
\binom mj\binom{k-m}{j}.
}
\tag{14}
\]

Since `\binom{k}{m}/Z_m(k)=1-O(m/k)` when `m=o(k)`, any termwise-absolute proof of `(3)` necessarily needs, for each fixed `j`,

\[
\boxed{
\eta_{2j}
\ll
L_y\frac{(j!)^2}{m^j k_y^j}
}
\tag{15}
\]

up to the displayed top-layer factor. At the live choice

\[
m=t+1,
\qquad
t=\left(\frac1{\log2}+o(1)\right)\log\log y,
\]

`MC-268` permits losses as large as

\[
L_y=o(k_y/m).
\]

Even under that generous allowance, `(15)` forces

\[
\boxed{
\eta_2=o(m^{-2}),
}
\tag{16}
\]

and for fixed `j`

\[
\boxed{
\eta_{2j}
=o\!\left(
\frac{(j!)^2}{m^{j+1}k_y^{j-1}}
\right).
}
\tag{17}
\]

At the opposite end the source-pair distribution is almost entirely on the top layer. When `m^2=o(k)`,

\[
\boxed{
w_{m,k}(2m)
=
\frac{\binom{k}{m}\binom{k-m}{m}}{Z_m(k)^2}
=1-O\!\left(\frac{m^2}{k}\right).
}
\tag{18}
\]

Yet `(13)` still requires, if that layer is controlled independently,

\[
\boxed{
\eta_{2m}
=o\!\left(\frac{m!}{m k_y^{m-1}}\right)
}
\tag{19}
\]

at the maximal useful loss scale. The reason is simple but important: the comparison baseline is not total probability one but the tiny diagonal atom `w_0=1/Z\asymp m!/k^m`.

The durable frontier correction is therefore twofold.

1. The Christoffel route should be attacked directly as the flat second-moment inequality `(4)`, where cancellation among all off-diagonal source pairs remains available.
2. Proving generic estimates for the individual radial quantities `H_d` and then summing their absolute values forfeits the main advantage of the Christoffel detector unless those estimates reach the precision ladder `(15)`–`(19)`.

This does not prove `(3)` or `(4)`, does not exclude a blind relation, and does not imply a new bound for `M(X)`. It identifies the exact analytic object and rules out a broad layerwise-absolute route at quantitatively ordinary levels of control.

## 1. Derivation of the flat energy

For a sign vector with `b` negative coordinates, the standard Boolean-cube identity is

\[
K_s(b;k)
=
\sum_{|S|=s}\prod_{p\in S}x_p.
\tag{20}
\]

Taking `x_p=\sigma_p(T)` and summing `(20)` over `0\le s\le m` yields

\[
R_m(b_y(T);k_y)
=
\sum_{S\in\mathcal B_m}\prod_{p\in S}\sigma_p(T)
=
\sum_{S\in\mathcal B_m}\chi_T(q_S).
\]

Division by `Z` proves `(1)`, and squaring then summing over the shell family proves `(2)`.

Expanding the square in `(2)`, the diagonal pairs `S=U` contribute one for every row `T`; there are exactly `Z` such pairs. This proves `(5)` and the equivalence of `(3)` with `(4)`.

For `S\ne U`, the product character is indexed by the symmetric difference:

\[
\chi_T(q_S)\chi_T(q_U)
=
\chi_T(q_{S\triangle U}).
\tag{21}
\]

Thus `(4)` is a genuine quadratic-character second moment, not an analogy to one.

## 2. Hamming-ball convolution gives the coefficients exactly

Square the Walsh expansion before evaluating at the arithmetic sign vector:

\[
P_m(x)^2
=
\frac1{Z^2}
\sum_{S,U\in\mathcal B_m}\chi_{S\triangle U}(x).
\tag{22}
\]

For any fixed support `V` of weight `d`, the coefficient of `\chi_V` is the number of `S\in\mathcal B_m` for which `S\triangle V\in\mathcal B_m`, namely `a_{m,k}(d)`. This coefficient depends only on `d`. Summing the characters of equal support size gives `K_d(b;k)`, proving `(7)` and `(8)`.

To count `(9)`, split `S` into `j=|S\cap V|` coordinates inside `V` and `\ell=|S\setminus V|` outside. The two ball conditions are

\[
j+\ell\le m,
\qquad
d-j+\ell\le m,
\]

so

\[
\ell\le m-\max(j,d-j).
\]

This proves `(9)`. Summing `\binom kd a_{m,k}(d)` over `d` counts all ordered pairs `(S,U)\in\mathcal B_m^2`, proving that `(10)` sums to one.

For `d=0`, `a_{m,k}(0)=Z`, which gives `(12)` and `(11)`.

## 3. The precision ladder is combinatorial, not heuristic

Fix a support `V` with `|V|=2j`. Restrict the count in `(6)` to sets `S` of size exactly `m` with

\[
|S\cap V|=j.
\]

Then `|S\triangle V|=m` as well, giving

\[
a_{m,k}(2j)
\ge
\binom{2j}{j}\binom{k-2j}{m-j}.
\]

Multiplying by `\binom{k}{2j}/Z^2` and dividing by `w_0=1/Z` yields `(14)` through the exact identity

\[
\binom{k}{2j}\binom{2j}{j}\binom{k-2j}{m-j}
=
\binom{k}{m}\binom mj\binom{k-m}{j}.
\]

Because all terms in the absolute-value majorant `(13)` are nonnegative, each individual even layer must fit inside the same total budget. Equations `(15)`–`(17)` follow from `(14)` and the usual fixed-`j` binomial asymptotics.

For `d=2m`, both ball members must have size exactly `m`, be disjoint, and partition the `2m` coordinates of the symmetric difference. Hence

\[
a_{m,k}(2m)=\binom{2m}{m},
\]

which gives the first equality in `(18)`. If `m^2=o(k)`, then

\[
Z_m(k)=\binom{k}{m}\left(1+O\!\left(\frac{m}{k}\right)\right)
\]

and

\[
\frac{\binom{k-m}{m}}{\binom{k}{m}}
=1-O\!\left(\frac{m^2}{k}\right),
\]

proving `(18)`. Applying `(14)` with `j=m` to `(13)` gives `(19)`.

These estimates were also checked by exact finite enumeration for small `(k,m)`; the stored claim does not rely on that computation.

## 4. Why the generic quadratic large sieve still misses the target

Equation `(4)` removes the Gaussian/Rademacher multiplicity penalty diagnosed in `MC-264`, but it does **not** make the known all-moduli quadratic large sieve strong enough.

Every source index obeys

\[
q_S\le y^m,
\]

while every row modulus lies in

\[
y^t<q_T\le(2y)^t.
\]

Embedding the rows into all square-free moduli and the flat source vector into all integers up to `y^m`, Heath-Brown's quadratic large sieve (and the explicit 2026 form of Liu) has the generic `(Q+M)` scale, up to its stated subpower loss. At the useful choice `m=t+1`, the source-length term is of order `y^{t+1}Z`, whereas the desired diagonal in `(4)` is only

\[
\binom{N_y}{t}Z
\asymp
\frac1{t!}\left(\frac{y}{\log y}\right)^t Z.
\]

The ratio is at least of order

\[
y\,t!\,(\log y)^t
\]

before the generic large-sieve loss is paid. The same sparse-family obstruction therefore survives the Christoffel lift, but in a cleaner form: the missing theorem is now a diagonal-scale large-sieve/orthogonality estimate for the **exact fixed-weight shell-product row family**, not a high-moment estimate with complicated tensor coefficients.

## 5. Prior art and novelty boundary

The finite harmonic-analysis mechanism is classical. Philip Feinsilver and René Schott, *Krawtchouk transforms and convolutions* (Bulletin of Mathematical Sciences, 2018/2019, DOI `10.1007/s13373-018-0132-2`, version of record also DOI `10.1142/S1664360719500097`), develops Krawtchouk transforms together with their convolution/linearization structure. Naomi Kirshner and Alex Samorodnitsky, *A Moment Ratio Bound for Polynomials and Some Extremal Properties of Krawchouk Polynomials and Hamming Spheres* (IEEE Transactions on Information Theory 67 (2021), 3509–3541, DOI `10.1109/TIT.2021.3071597`), studies Krawtchouk extremality and pair-distance structure in Hamming spheres/balls. Thus `(7)`–`(10)` are treated as a classical Boolean-cube convolution mechanism specialized to the `MC-268` detector, not as a new coding-theory result.

Sparse-modulus large sieves are also established prior art. Stephan Baier, *On the large sieve with sparse sets of moduli* (J. Ramanujan Math. Soc. 21 (2006), 279–295), develops a general sparse-moduli framework, and Henryk Iwaniec, *The large sieve with prime moduli* (Rev. Mat. Iberoam. 38 (2022), 2337–2354, DOI `10.4171/RMI/1381`), obtains true-order estimates for a different prime-modulus setting. Zihao Liu's *Explicit quadratic large sieve inequality* (Acta Arith. 223 (2026), 227–252, DOI `10.4064/aa250722-27-1`) gives an explicit Heath-Brown quadratic large sieve and remains the direct generic quadratic-character comparison already used in `MC-262` and `MC-264`.

A targeted literature search through 13 September 2026 found no theorem that supplies `(4)` at diagonal scale for the simultaneous combination present here: quadratic characters with row moduli equal to fixed-weight products of shell primes and a flat coefficient set equal to products of at most `m\asymp\log\log y` lower primes. This is a search boundary, not a proof of novelty or nonexistence.

The durable Mathia delta is therefore the exact specialization: the endpoint-optimal detector of `MC-268` is a flat sparse quadratic large-sieve energy with an explicit natural diagonal, and its radial Krawtchouk decomposition has a severe absolute-value precision ladder. This identifies what an arithmetic theorem must preserve and why generic per-layer estimates can destroy the detector's gain.

## 6. Boundaries and decisive consequence

- **No blind relation is excluded.** Equations `(3)` and `(4)` remain unproved arithmetic estimates.
- **No new global Möbius bound follows.** The downstream generation-to-`M(X)` transfer remains separate.
- **No novelty is claimed for Krawtchouk convolution, Hamming-ball intersection numbers, Christoffel extremality, or generic/sparse large-sieve theory.**
- **The termwise obstruction is proof-method specific.** Signed cancellation among the `h_d` or direct operator/large-sieve control of `(2)` can evade `(15)`–`(19)`.
- **The generic all-moduli embedding remains too expensive.** A successful analytic theorem must exploit the exact shell-product/source-ball structure rather than only the maximum modulus and coefficient length.

The next decisive test is correspondingly precise: prove a nontrivial bound for the flat energy `(4)` directly over the fixed-weight shell family—ideally with `L_y=o(k_y/m)` at `m=t+1`—or derive an admissible arithmetic lower-bound/counterexample showing that this diagonal-scale target itself cannot hold. Universal Krawtchouk identities alone cannot decide that question.