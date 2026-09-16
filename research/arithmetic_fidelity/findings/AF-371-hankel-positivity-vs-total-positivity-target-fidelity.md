# AF-371 — Hankel positivity is not target-faithful for real-zero structure; translation total positivity is

**Status:** `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `TARGET-FIDELITY`, `POSITIVITY`, `TOTAL-POSITIVITY`, `LAGUERRE-POLYA`, `PRIOR-ART-REDIRECT`, `NO-NOVELTY-CLAIM`

## Claim

There is a sharp classical separation between two positivity summaries attached to a real entire function.

Let `Psi` be an entire function with `Psi(0)>0`, not a pure exponential, and write near the origin

\[
\frac{1}{\Psi(s)}=\sum_{j\ge 0}\frac{\gamma_j}{j!}s^j.
\tag{1}
\]

If `Psi` belongs to the Laguerre–Pólya class, then every finite Hankel matrix

\[
H_n(\Psi)=\big(\gamma_{j+k}\big)_{j,k=0}^{n-1}
\tag{2}
\]

is positive definite. However Hamburger proved that positivity of all these Hankel matrices is **not sufficient** to force `Psi` into the Laguerre–Pólya class. Thus the Boolean signature

\[
\mathcal H(\Psi)=\{H_n(\Psi)\succ0\text{ for every }n\}
\tag{3}
\]

is not target-faithful for the property

\[
\mathcal L(\Psi)=\{\Psi\in LP\}.
\tag{4}
\]

By contrast, Schoenberg's characterization is exact. A function `Psi` in the Laguerre–Pólya class with `Psi(0)>0` has reciprocal equal, on its strip of convergence, to the bilateral Laplace transform of a Pólya-frequency function `Lambda`; conversely every such Pólya-frequency transform has reciprocal denominator in the Laguerre–Pólya class. The defining condition is relational total positivity:

\[
\det\!\big(\Lambda(x_j-y_k)\big)_{j,k=1}^{m}\ge0
\tag{5}
\]

for every `m` and every increasing `x_1<...<x_m`, `y_1<...<y_m`, together with integrability.

Therefore the classical theory supplies an exact Arithmetic Fidelity example in which an **infinite hierarchy of ordinary positive-definiteness tests remains a false-positive certificate**, while a stronger ordered relational positivity structure is equivalent to the desired target property.

The point is about **target-property certification**, not source reconstruction. The complete Taylor sequence `(gamma_j)` determines the analytic germ `1/Psi` and hence `Psi`; no claim is made that the coefficients themselves have lost the source. What loses discrimination is the compression of that rich data to the positivity verdicts `(3)`. This separates two notions that should not be conflated:

- source fidelity: whether retained data determine the original object;
- target fidelity: whether a specified compressed certificate decides the property of interest.

An observation can be source-rich while a chosen downstream positivity summary is target-poor.

## Classical derivation

Gröchenig's modern account records the Pólya–Schur necessary condition: if `Psi` is in the Laguerre–Pólya class, `Psi(0)>0`, and `1/Psi` has expansion `(1)`, then every matrix `(2)` is positive definite. He immediately notes the classical obstruction: Hamburger's 1920 paper proved that positivity of the entire Hankel hierarchy is not sufficient for membership in the Laguerre–Pólya class.

Hamburger's result can be read through the moment problem. With the sign convention

\[
\frac{1}{\Psi(s)}=\sum_{j\ge0}\mu_j\frac{(-s)^j}{j!},
\tag{6}
\]

positivity of all principal Hankel determinants implies that `1/Psi` is the bilateral Laplace transform of a nonnegative function or measure with moments `mu_j` on the maximal strip of regularity. Positivity therefore recovers **nonnegative representability**, but it does not force the much stronger translation-determinant constraints `(5)`.

Schoenberg closes exactly that gap. For an integrable nontrivial `Lambda`, the translation kernel

\[
K_\Lambda(x,y)=\Lambda(x-y)
\tag{7}
\]

is totally nonnegative at every finite order precisely in the Pólya-frequency setting, and its bilateral Laplace transform is `1/Psi` for a Laguerre–Pólya entire function `Psi`. Conversely a Laguerre–Pólya `Psi` with `Psi(0)>0` produces such a Pólya-frequency `Lambda`.

Hence Hamburger and Schoenberg together produce the strict implication pattern

\[
\text{translation total positivity}
\Longleftrightarrow
\Psi\in LP
\Longrightarrow
\text{all Hankel matrices positive},
\tag{8}
\]

while the reverse implication on the right fails.

This is stronger than the generic statement that "positivity may lose information." Both sides impose infinitely many positivity constraints. The decisive difference is **which relations the minors see**: Hankel moment matrices test quadratic positivity of a scalar moment sequence, whereas total positivity tests all ordered cross-relations of the translation kernel.

## Fidelity interpretation

Define the target discriminator

\[
D(\Psi)=\mathbf 1_{\{\Psi\in LP\}}.
\tag{9}
\]

Define a coarse positivity certificate `C_H` that remembers only whether every Hankel matrix `(2)` is positive definite. Hamburger gives a nontrivial fiber collision:

\[
D(\Psi_1)=1,\qquad D(\Psi_0)=0,
\qquad C_H(\Psi_1)=C_H(\Psi_0)=\text{true}
\tag{10}
\]

for suitable admissible entire functions. Thus `D` does not factor through `C_H`.

Now replace that certificate by the existence of the reciprocal Laplace representation with an integrable kernel satisfying all translation minors `(5)`. Schoenberg gives

\[
D(\Psi)=C_{TP}(\Psi).
\tag{11}
\]

So `C_TP` is target-faithful on the stated class. This is an exact **certificate lift**: one moves from scalar/moment positive definiteness to ordered relational total positivity, and the false-positive fiber disappears.

No minimality claim is made. Schoenberg supplies an exact lift, not a theorem that every smaller relational family must fail. The durable lesson is narrower: increasing the number of scalar positivity tests all the way to an infinite hierarchy does not compensate for testing the wrong relational geometry.

## Riemann specialization

For

\[
\Xi(t)=\xi\!\left(\tfrac12+it\right),
\tag{12}
\]

the Riemann hypothesis is equivalent to `Xi` belonging to the Laguerre–Pólya class. Gröchenig combines this with Schoenberg's theorem to obtain the exact equivalence: RH holds if and only if the reciprocal transform associated with `1/Xi` is a Pólya-frequency function; equivalently, the corresponding translation kernel satisfies total positivity at every finite order.

This does **not** say that RH follows from Hankel positivity of the reciprocal Taylor coefficients. Hamburger's counterexample is precisely why that replacement is invalid as a general criterion. It also does not assert that the relevant low-order positivity conditions for `Xi` are known: Gröchenig explicitly remarks that even the first nontrivial positivity consequences for `1/xi` are not presently available in a form that makes the criterion useful.

The Riemann case is therefore an application of the abstract fidelity separation, not evidence for RH. It demonstrates why a route that turns arithmetic structure into generic PSD or moment positivity may preserve too weak a certificate even when infinitely many inequalities survive.

## Prior-art and novelty audit

- Hans Ludwig Hamburger, **“Bemerkungen zu einer Fragestellung des Herrn Pólya,”** *Mathematische Zeitschrift* **7** (1920), 302–322. Role: proves that the positive Hankel-determinant conditions arising from Pólya's necessary criterion are not sufficient to recover the Laguerre–Pólya class, while connecting them to Laplace/moment representations.
- I. J. Schoenberg, **“On Totally Positive Functions, Laplace Integrals and Entire Functions of the Laguerre-Polya-Schur Type,”** *Proceedings of the National Academy of Sciences USA* **33** (1947), 11–17, DOI `10.1073/pnas.33.1.11`. Role: early statement of the reciprocal Laplace-transform correspondence between total positivity and Laguerre–Pólya entire functions.
- I. J. Schoenberg, **“On Pólya Frequency Functions. I. The Totally Positive Functions and Their Laplace Transforms,”** *Journal d'Analyse Mathématique* **1** (1951), 331–374, DOI `10.1007/BF02790092`. Role: classical full characterization of Pólya-frequency functions by reciprocal Laguerre–Pólya Laplace transforms.
- Karlheinz Gröchenig, **“Schoenberg's Theory of Totally Positive Functions and the Riemann Zeta Function,”** arXiv:`2007.12889` (2020). Role: modern exposition of Schoenberg's theorem, the Pólya–Schur/Hamburger Hankel-positivity boundary, and the exact Riemann-`Xi`/Pólya-frequency equivalence.
- Alexander Belton, Dominique Guillot, Apoorva Khare and Mihai Putinar, **“Preservers of Totally Positive Kernels and Pólya Frequency Functions,”** *Mathematics Research Reports* **3** (2022), 35–56, DOI `10.5802/mrr.12`. Role: modern authoritative survey of Pólya-frequency functions and Schoenberg's transform characterization.

No novelty is claimed for the Laguerre–Pólya criteria, the moment problem, Hamburger's insufficiency theorem, Schoenberg's transform theorem, or the RH equivalence. The Arithmetic Fidelity contribution is the explicit **source-fidelity versus target-fidelity accounting** and the identification of total positivity as a relational lift that closes a false-positive fiber left open by an infinite Hankel-positivity summary.

## Decisive audit rule

When a proposed arithmetic compression ends in positivity, do not measure the retained information by the number of inequalities alone. Identify the exact target property and ask whether it factors through the chosen positivity signature.

For real-zero/Laguerre–Pólya targets, ordinary Hankel/moment positivity is only a necessary certificate and admits false positives. A valid claim of target fidelity needs stronger structure; Schoenberg's translation total positivity gives one exact classical benchmark. In particular, replacing lost arithmetic orientation or provenance by ever more PSD moment constraints cannot be justified merely by the hierarchy being infinite.