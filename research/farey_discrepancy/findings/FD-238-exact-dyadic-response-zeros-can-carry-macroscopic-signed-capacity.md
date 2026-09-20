# FD-238 — Exact dyadic-response zeros can carry macroscopic signed capacity

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response kernel / signed capacity / exact dyadic nullspace / block balancing / positivity boundary / response-topology diagnostic
- **Depends on:** FD-225, FD-230, FD-231, FD-233, FD-237
- **Classification:** `EXACT-DERIVED + COUNTERMODEL + SIGNED-LINEAR-CAPACITY + EXACT-DYADIC-SWITCHED-NULLSPACE + MACROSCOPIC-TOTAL-VARIATION + POSITIVITY-BOUNDARY`

## Claim

FD-231 constructs signed linear-capacity profiles whose full divisor response is only linear, so the dyadic switched rows are far below their natural quadratic scale. The same phenomenon can be made exact on every dyadic switched row. There exists an integer sequence `(b_n)` such that

\[
\boxed{|b_n|\le n\qquad(n\ge1),}
\tag{1}
\]

its divisor response

\[
(\mathscr A b)(m)
=
\sum_{d\le m} b_d M\!\left(\left\lfloor\frac md\right\rfloor\right)
\tag{2}
\]

obeys

\[
\boxed{(\mathscr A b)(2^j)=0\qquad(j\ge0),}
\tag{3}
\]

and therefore, with `(TF)(m)=F(2m)`, every fixed finite-difference row vanishes exactly at every dyadic base point:

\[
\boxed{
((T-I)^r\mathscr A b)(2^j)=0
\qquad(j\ge0,\ r\ge1).
}
\tag{4}
\]

In particular, all switched rows used in FD-212--FD-237, including the scheduler orders `r=1` and `r=4`, are identically zero on this profile.

This exact invisibility does not come from a small coefficient vector. On dyadic bands

\[
B_k=(2^{k-1},2^k]\cap\mathbb N,
\]

one has

\[
\boxed{
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}|b_n|}
     {\sum_{n\in B_k}n}
\ge
\frac{12}{\pi^2}-1
\approx0.21585.
}
\tag{5}
\]

Moreover both signs remain macroscopic:

\[
\boxed{
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}b_n^+}
     {\sum_{n\in B_k}n},
\quad
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}b_n^-}
     {\sum_{n\in B_k}n}
\ge
\frac12\left(\frac{12}{\pi^2}-1\right).
}
\tag{6}
\]

Thus the exact kernel of the entire family of dyadic switched stencils already contains integer signed profiles carrying a fixed positive fraction of linear reservoir capacity. Any refinement that keeps exactly the same dyadic response coordinates and merely strengthens their scalar normalization cannot control signed repair geometry: these directions remain zero under every normalization. What survives as a possible coercive mechanism is the one-sided/nonnegative geometry isolated in FD-230--FD-233, or genuinely additional response coordinates such as off-dyadic/all-integer or source-forced observables.

This is not a physical nonnegative occupancy countermodel. The profile `b` has both signs at macroscopic density. Its role is to identify an exact signed nullspace that any future positivity or source-realizability argument must quotient out or detect with additional coordinates.

## 1. Exact block-balanced source for the divisor transform

For any arithmetic function `g`, set

\[
b=\mathbf 1*g,
\qquad
b_n=\sum_{d\mid n}g(d).
\tag{7}
\]

Since `mu*1=epsilon`, expanding the Mertens function in `(2)` gives the exact identity

\[
\begin{aligned}
(\mathscr A b)(m)
&=
\sum_{d\le m}b_d
\sum_{q\le m/d}\mu(q)\\
&=
\sum_{n\le m}(b*\mu)(n)\\
&=
\boxed{\sum_{n\le m}g(n).}
\end{aligned}
\tag{8}
\]

Hence it suffices to build an integer `g` with linear pointwise envelope, substantial magnitude, and zero cumulative sum at every dyadic endpoint.

Put `g(1)=0`. For each block

\[
I_k=(2^{k-1},2^k]\cap\mathbb N,
\qquad k\ge1,
\tag{9}
\]

choose a pivot `e_k in I_k` for which `phi(e_k)` is maximal. Process all nonpivot integers of `I_k` in increasing order. At a nonpivot `n`, choose

\[
g(n)\in\{-\varphi(n),+\varphi(n)\}
\tag{10}
\]

with sign opposite to the current nonpivot partial sum. If

\[
W_k=
\max_{n\in I_k\setminus\{e_k\}}\varphi(n),
\]

then the elementary one-dimensional greedy balancing step preserves

\[
|S|\le W_k:
\qquad
|S'|=\bigl||S|-\varphi(n)\bigr|\le W_k.
\tag{11}
\]

Let `S_k` be the final sum of all nonpivot values and define

\[
\boxed{g(e_k)=-S_k.}
\tag{12}
\]

The choice of pivot gives

\[
|g(e_k)|=|S_k|\le W_k\le\varphi(e_k).
\tag{13}
\]

All values are integers, `|g(n)|<=phi(n)`, and every block sums exactly to zero:

\[
\boxed{
\sum_{n\in I_k}g(n)=0.
}
\tag{14}
\]

Writing

\[
Y(m)=\sum_{n\le m}g(n),
\tag{15}
\]

we therefore have

\[
\boxed{Y(2^j)=0\qquad(j\ge0).}
\tag{16}
\]

The same greedy estimate also controls values between endpoints. Before the pivot the running block sum has modulus at most `W_k`; after inserting the pivot it is a difference of two nonpivot partial sums, hence at most `2W_k`. Since `W_k<=2^k`,

\[
\boxed{Y(m)=O(m).}
\tag{17}
\]

By `(8)`, `mathscr A b=Y`.

## 2. Linear capacity and exact switched invisibility

Equation `(7)` and `|g(d)|<=phi(d)` imply, using the classical divisor identity `sum_{d|n} phi(d)=n`,

\[
|b_n|
\le
\sum_{d\mid n}|g(d)|
\le
\sum_{d\mid n}\varphi(d)
=
\boxed n.
\tag{18}
\]

At each dyadic point `(16)` and `(8)` give `(3)`. For any fixed `r>=1`,

\[
((T-I)^rY)(2^j)
=
\sum_{t=0}^r
(-1)^{r-t}\binom rtY(2^{j+t})
=0,
\tag{19}
\]

which proves `(4)`. This is stronger than the `O(m)` switched invisibility of FD-231: the selected response coordinates are now exactly zero, while the off-dyadic full response remains only linearly bounded by `(17)`.

The distinction is structural. The exact kernel in `(4)` survives any scalar renormalization of those same coordinates. Detecting this profile requires either a one-sided coefficient restriction or coordinates not contained in the dyadic switched stencil family.

## 3. A fixed fraction of signed capacity survives

For every nonpivot `n`, equation `(10)` has `|g(n)|=phi(n)`. Separating the top divisor in `(7)` gives

\[
\begin{aligned}
|b_n|
&\ge
|g(n)|-
\sum_{\substack{d\mid n\\d<n}}|g(d)|\\
&\ge
\varphi(n)-
\sum_{\substack{d\mid n\\d<n}}\varphi(d)\\
&=
\boxed{2\varphi(n)-n}.
\end{aligned}
\tag{20}
\]

There is only one pivot in each block. Omitting it from `(20)` changes the resulting lower bound by at most `O(2^k)`. The standard summatory totient asymptotic

\[
\sum_{n\le x}\varphi(n)
=
\frac{3}{\pi^2}x^2+O(x\log x)
\tag{21}
\]

and

\[
\sum_{n\in B_k}n
=
\frac38\,4^k+O(2^k)
\tag{22}
\]

therefore give

\[
\sum_{n\in B_k}|b_n|
\ge
\left(
\frac{9}{2\pi^2}-\frac38
\right)4^k
+o(4^k).
\tag{23}
\]

Dividing `(23)` by `(22)` proves `(5)`.

It remains to see that the mass is not asymptotically concentrated in one sign. Let

\[
B(x)=\sum_{n\le x}b_n.
\]

Using `(7)` and Abel summation with `Y(d)=O(d)`,

\[
B(x)
=
\sum_{d\le x}g(d)\left\lfloor\frac xd\right\rfloor
=
Y(x)
+
\sum_{d<x}Y(d)
\left(
\left\lfloor\frac xd\right\rfloor
-
\left\lfloor\frac{x}{d+1}\right\rfloor
\right).
\tag{24}
\]

Since

\[
\sum_{d\le x}
 d
\left(
\left\lfloor\frac xd\right\rfloor
-
\left\lfloor\frac{x}{d+1}\right\rfloor
\right)
\le
\sum_{d\le x}\left\lfloor\frac xd\right\rfloor
=O(x\log x),
\tag{25}
\]

we obtain

\[
\boxed{B(x)=O(x\log x).}
\tag{26}
\]

Thus the signed sum over `B_k` is `O(k2^k)=o(4^k)`, whereas `(5)` gives absolute mass `Omega(4^k)`. Since

\[
\sum b_n^+
=
\frac12\left(\sum|b_n|+\sum b_n\right),
\qquad
\sum b_n^-
=
\frac12\left(\sum|b_n|-\sum b_n\right),
\tag{27}
\]

both signs inherit half of the asymptotic lower density in `(5)`, proving `(6)`.

## 4. Consequences for the current frontier

FD-230 shows that nonnegative switched-null occupancies cannot retain positive dyadic capacity density. FD-231 shows that signed profiles can evade that coercivity with an `O(m)` response. The present construction strengthens the signed side to an exact statement: the common kernel of all dyadic switched stencils already contains integer, linear-envelope directions with macroscopic positive and negative mass.

Consequently, replacing the response normalization used in FD-233--FD-237 by any stronger scalar normalization on the same dyadic rows cannot remove these directions. A zero coordinate remains zero. Any response topology capable of controlling signed representatives must genuinely add information, for example by retaining off-dyadic/all-integer response values or source-forced coordinates. Alternatively, a proof can remain on the existing dyadic response space only if it uses the one-sided/nonnegative cone in an essential way.

This also clarifies why the obstruction isolated in FD-232--FD-237 is intrinsically one-sided. The signed nullspace is not merely large in an abstract norm; it intersects the natural integer linear-capacity box with a fixed positive density in both signs. The remaining physical question is therefore not whether the switched map has enough signed coercivity—it does not—but whether the concrete Mertens repair class can approach the nonnegative cone after quotienting by these exact blind directions.

## Prior-art / dependency note

No new external load-bearing input is introduced. The proof uses the elementary identities `mu*1=epsilon` and `sum_{d|n} phi(d)=n`, the standard summatory totient asymptotic already used in FD-231, and one-dimensional greedy sign balancing proved directly above. The construction is asserted only as a new diagnostic within this research line; no general literature-priority claim is made for the underlying balancing or convolution identities.

## Status

**Proved.** Exact source-side construction, exact divisor-transform identity, exact vanishing of every dyadic switched stencil, and asymptotic signed-capacity lower bounds are established above. The result is a signed countermodel/response-topology obstruction, not a realizable nonnegative prime-occupancy source and not progress toward RH by itself.
